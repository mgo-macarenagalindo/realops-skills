#!/usr/bin/env node
// Render a self-contained HTML share-image canvas to a flat JPG (or PNG) with
// headless Chrome, then check it for the usual problems: content spilling off the
// canvas, a page that scrolls, and web fonts that never loaded.
//
// Usage:
//   node render.mjs --html <file.html> --out <og-slug.jpg> [options]
//
// Options:
//   --width   <px>   Canvas width          (default 1200)
//   --height  <px>   Canvas height         (default 630)
//   --scale   <n>    Device scale factor   (default 2 → 2400×1260)
//   --quality <n>    JPEG quality 1–100    (default 85; ignored for .png)
//   --channel <name> chrome | msedge | chromium (default: chrome, then Playwright's Chromium)
//
// Prints the output path on the last stdout line. Warnings go to stderr, and the
// exit code is 3 when a check failed (the image is still written so you can look).

import { chromium } from 'playwright-core';
import { statSync, existsSync } from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

function parseArgs(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith('--')) out[a.slice(2)] = argv[++i];
  }
  return out;
}

async function launchBrowser(channel) {
  const attempts = channel ? [channel] : ['chrome', 'chromium'];
  let lastError;
  for (const ch of attempts) {
    try {
      return await chromium.launch(ch === 'chromium' ? {} : { channel: ch });
    } catch (e) {
      lastError = e;
    }
  }
  throw new Error(
    `Failed to launch a browser (tried ${attempts.join(', ')}). Install Google Chrome, or run ` +
    `"npx playwright install chromium" in the skill's scripts/ folder.\nUnderlying error: ${lastError && lastError.message}`
  );
}

async function main() {
  const a = parseArgs(process.argv.slice(2));
  if (!a.html || !a.out) {
    console.error('Required: --html <file.html> --out <file.jpg|file.png>. See the file header for options.');
    process.exit(2);
  }
  const htmlPath = path.resolve(a.html);
  if (!existsSync(htmlPath)) {
    console.error(`No such file: ${htmlPath}`);
    process.exit(2);
  }
  const outPath = path.resolve(a.out);
  const width = parseInt(a.width || '1200', 10);
  const height = parseInt(a.height || '630', 10);
  const scale = parseFloat(a.scale || '2');
  const quality = parseInt(a.quality || '85', 10);
  const type = outPath.toLowerCase().endsWith('.png') ? 'png' : 'jpeg';

  const browser = await launchBrowser(a.channel);
  const warnings = [];
  try {
    const context = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: scale });
    const page = await context.newPage();
    const failed = [];
    page.on('requestfailed', (req) => failed.push(req.url()));
    page.on('response', (res) => { if (res.status() >= 400) failed.push(`${res.status()} ${res.url()}`); });

    await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'networkidle', timeout: 30000 })
      .catch(() => page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'load', timeout: 30000 }));
    await page.evaluate(() => document.fonts.ready);

    const report = await page.evaluate(({ width, height }) => {
      const body = document.body.getBoundingClientRect();
      const overflow = [];
      for (const el of document.body.querySelectorAll('*')) {
        const r = el.getBoundingClientRect();
        if (!r.width || !r.height) continue;
        const style = getComputedStyle(el);
        if (style.visibility === 'hidden' || style.display === 'none') continue;
        if (el.closest('[data-bleed]')) continue; // intentional full-bleed/cropped visuals
        if (r.left < -1 || r.top < -1 || r.right > width + 1 || r.bottom > height + 1) {
          const label = el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).join('.') : '');
          overflow.push(`${label} (${Math.round(r.left)},${Math.round(r.top)} → ${Math.round(r.right)},${Math.round(r.bottom)})`);
        }
      }
      // Check each family/weight/style combination that actually renders text.
      const faces = new Map();
      for (const el of document.body.querySelectorAll('*')) {
        const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
        if (!hasText) continue;
        const cs = getComputedStyle(el);
        const family = cs.fontFamily.split(',')[0].trim().replace(/^["']|["']$/g, '');
        faces.set(`${cs.fontStyle} ${cs.fontWeight} 16px "${family}"`, family);
      }
      const generic = new Set(['serif', 'sans-serif', 'monospace', 'system-ui', 'cursive', 'fantasy', 'ui-sans-serif', 'ui-serif', '-apple-system']);
      const missingFonts = [...new Set([...faces].filter(([font, family]) => !generic.has(family) && !document.fonts.check(font)).map(([font]) => font))];
      const headline = document.querySelector('[data-headline], h1');
      let headlineLines = null;
      if (headline) {
        const lh = parseFloat(getComputedStyle(headline).lineHeight) || parseFloat(getComputedStyle(headline).fontSize) * 1.2;
        headlineLines = Math.round(headline.getBoundingClientRect().height / lh);
      }
      return {
        wrongSize: Math.round(body.width) !== width || Math.round(body.height) !== height || getComputedStyle(document.body).overflow !== 'hidden',
        overflow: overflow.slice(0, 10),
        missingFonts,
        headlineLines,
      };
    }, { width, height });

    if (report.wrongSize) warnings.push(`Pin body to exactly ${width}×${height} with overflow:hidden; anything outside the canvas is cropped.`);
    if (report.overflow.length) warnings.push(`Elements spill off the canvas (mark intentional full-bleed visuals with data-bleed):\n    ${report.overflow.join('\n    ')}`);
    if (report.missingFonts.length) warnings.push(`Fonts not loaded, a fallback was used: ${report.missingFonts.join(', ')}`);
    if (report.headlineLines && report.headlineLines > 2) warnings.push(`Headline wraps to ${report.headlineLines} lines; keep it to 2 (shorten it or lower its font size).`);
    if (failed.length) warnings.push(`Assets failed to load:\n    ${[...new Set(failed)].slice(0, 10).join('\n    ')}`);

    const shot = { path: outPath, type, clip: { x: 0, y: 0, width, height } };
    if (type === 'jpeg') shot.quality = quality;
    await page.screenshot(shot);
    await context.close();
  } finally {
    await browser.close();
  }

  const kb = Math.round(statSync(outPath).size / 1024);
  console.error(`Rendered ${Math.round(width * scale)}×${Math.round(height * scale)} ${type.toUpperCase()}, ${kb} KB`);
  if (kb > 1024) warnings.push(`File is ${kb} KB; some platforms drop share images over ~1 MB. Lower --quality or use --scale 1.`);
  for (const w of warnings) console.error(`WARNING: ${w}`);
  console.log(outPath);
  if (warnings.length) process.exit(3);
}

main().catch((err) => {
  console.error(`render error: ${err.message}`);
  process.exit(1);
});
