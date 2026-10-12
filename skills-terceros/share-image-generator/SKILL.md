---
name: share-image-generator
description: Generates a per-page Open Graph / social share image (the picture shown when a link is posted on LinkedIn, X, Slack, iMessage) as a flat 2400×1260 JPG in the user's own brand colors and logo, rendered from a self-contained 1200×630 HTML canvas with headless Chrome. Use when the user asks for an "OG image", "share image", "social card", "Twitter card", "og:image", "link preview image", or "make a share image for <page>". Takes headline, brand colors, logo and an optional product screenshot as input, checks the render for clipped text and missing fonts, saves the JPG into the project's static folder and gives the meta tags to wire in.
---

# Share Image Generator

Makes the image that appears when one of the user's pages is shared: a flat JPG built from a 1200×630 HTML canvas in the user's brand, rendered at 2× for retina.

- Design rules (canvas, layouts, type, contrast, copy, meta tags): [references/design.md](references/design.md). **Read it before writing the HTML.**
- Starting canvas with the three layouts: [assets/template.html](assets/template.html).
- Renderer and checker: `scripts/render.mjs`.

`<skill-dir>` below means the folder this SKILL.md is in.

## Workflow

```
- [ ] Step 1: Gather the inputs (page, headline, brand colors, logo, visual)
- [ ] Step 2: Pick the layout and output path
- [ ] Step 3: Write the HTML canvas from the template
- [ ] Step 4: Render and fix every warning
- [ ] Step 5: Look at the image, then report the file and the meta tags
```

### Step 1: Gather the inputs

The image is built from the **user's** brand, never a default theme and never another company's assets.

1. **Page and headline.** Which page is this for? Take the headline from what the user said, else the page's H1 or `<title>`. Tighten to ≤ 8 words if needed, without adding claims (see the Copy section of the design reference).
2. **Brand colors**: background, text, and primary/accent. If the user gave them, use them as given.
3. **Logo**: a file path or URL to an SVG or PNG. If there isn't one, use a text wordmark of the product name in the brand font.
4. **Font**: the font the site uses.
5. **Product visual** (optional): a screenshot or image of the product for the split or peek layouts.

If the user didn't give colors or a logo, look in the project for them: CSS custom properties, the Tailwind theme or config, a `theme`/`tokens` file, and logo files in `public/`, `static/`, `assets/` or `src/assets/`. **Show the user what you found** (hex values, the logo file path, the font) and ask them to confirm or give their own, in one short question. If there is no project and nothing was given, ask for the colors and logo before rendering. Don't invent a palette.

For a product visual of a live page, the `screenshot-capture` skill (or any headless browser) can grab one.

### Step 2: Layout and output path

- **Layout**: `layout-centered` by default; `layout-split` or `layout-peek` when there is a good product visual. If the user is unsure, render two layouts and let them pick.
- **Slug**: kebab-case from the page (`pricing`, `blog-why-we-raised`, `home`).
- **Output folder** = the project's static folder, served at the site root:

| Project | Folder |
|---|---|
| Next.js, Vite, Nuxt 3+, Astro, Remix, Create React App | `public/` |
| SvelteKit, Hugo, Nuxt 2, Gatsby | `static/` |
| Plain HTML site | next to `index.html`, or its `images/` folder |
| No project | the current directory |

  Output file: `<folder>/og-<slug>.jpg`. If the project already has share images, match their folder and naming instead.

- **Canvas HTML**: `.share-images/og-<slug>.html` in the project root (keep it so the image can be regenerated; suggest adding `.share-images/` to `.gitignore` if the user doesn't want it committed).

### Step 3: Write the canvas

Copy `<skill-dir>/assets/template.html` to the canvas path and edit it:

- Set the CSS variables in `:root` to the brand inputs.
- Set the font: a Google Fonts `<link>` if it's a Google font, or an `@font-face` pointing at the project's own font file with a path relative to the HTML file.
- Put the logo in `.logo`: paste the SVG markup inline (best: no path issues, inherits color), or an `<img>` with a path **relative to the HTML file** (e.g. `../public/logo.svg`). Copying the logo next to the HTML also works.
- Write the headline into the `h1` (keep `data-headline`) and the subline or proof into `.sub`, or delete `.sub`.
- Keep one layout; delete the commented ones you didn't use.

Hard rules: one self-contained HTML file, inline `<style>`, no JS, no frameworks, no animation. Body exactly 1200×630 with `overflow: hidden`. Images that intentionally run off the edge get `data-bleed`.

### Step 4: Render

First run only: `cd <skill-dir>/scripts && npm install` (installs `playwright-core`; it drives the installed Google Chrome, or Playwright's Chromium via `npx playwright install chromium`).

```bash
node <skill-dir>/scripts/render.mjs --html .share-images/og-<slug>.html --out public/og-<slug>.jpg
```

The last stdout line is the output path. The script exits with code 3 and prints `WARNING:` lines when something is off:

- **Elements spill off the canvas**: shorten the copy or reduce the font size; mark intentional bleeds with `data-bleed`.
- **Headline wraps to 3+ lines**: shorten it, then step the font size down 4px at a time (not below 52px).
- **Fonts not loaded**: fix the font link or `@font-face` path; never ship a fallback-font render.
- **Assets failed to load**: fix the logo or visual path (relative to the HTML file).
- **File over ~1 MB**: add `--quality 78` or `--scale 1`.

Fix and re-render until there are no warnings.

### Step 5: Check and report

Open the JPG and run the quality checks from the design reference: the headline reads first and at a glance, nothing touches the edges, real brand font, strong contrast. Re-render if anything is off.

Report:

- The image path and its size (2400 × 1260)
- The canvas HTML path (to regenerate later)
- The meta tags for the page, with the absolute URL on the user's domain (see **Meta tags** in the design reference). Offer to add them to the page; edit the page only if the user says yes.

For a set of pages, reuse the same canvas with only the headline (and visual) changed, so the cards look like one brand.
