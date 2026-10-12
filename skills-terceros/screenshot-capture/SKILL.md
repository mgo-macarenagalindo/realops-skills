---
name: screenshot-capture
description: Captures a PNG of any rendered web page in headless Chrome — the whole page, one section, a single element, the above-the-fold viewport, or a mobile/tablet/desktop rendering. Use when the user says "screenshot", "take a screenshot", "grab a screenshot of <url>", "screenshot the hero / pricing / nav / that button", "show me how X renders", "screenshot the mobile view", or when another task needs a before/after capture of a page. Infers the target from plain language, resolves sections by heading text, CSS selector or Nth <section>, saves a PNG and shows it. Self-contained: drives the installed Google Chrome (or Playwright's Chromium) through playwright-core, no MCP server.
---

# Screenshot Capture

Loads a URL in headless Chrome and captures exactly what the user asked for: the whole page, one section, a single element, the viewport, or a specific device size. Saves a PNG and opens it so the result is visible.

The engine is `scripts/screenshot.mjs` in this skill's folder. It drives the installed Google Chrome through `playwright-core` (no bundled browser download) and falls back to Playwright's own Chromium if Chrome isn't there. It prints the saved PNG path on its **last stdout line**: read that path, then open the PNG to view it.

Below, `<skill-dir>` means the folder this SKILL.md is in (for example `.claude/skills/screenshot-capture`, `.agents/skills/screenshot-capture`, or `~/.codex/skills/screenshot-capture`, depending on where it was installed).

## When to use this skill

- "Screenshot localhost:3000" / "grab a screenshot of example.com"
- "Screenshot the pricing section" / "capture the hero" / "the footer"
- "Screenshot the CTA button" / "just the nav bar" / "the `.testimonials` block"
- "Screenshot the whole page" / "the full scrollable page"
- "Screenshot the mobile view" / "how does this look on tablet"
- Before/after captures for a design, audit or responsive pass

## When NOT to use this skill

- The user wants to **interact** with the page (click through a flow, fill forms, check console or network): use a browser-testing tool.
- The user wants a **generated design or mockup**, not a capture of a real page.
- A screenshot of the desktop or a native app: out of scope.

## Rules

- **Interpret intent first.** The user describes *what* in plain language; you pick the flag (map below). Don't ask which flag.
- **The last stdout line is the PNG path** (everything else goes to stderr). Capture it and open the image.
- **Report the full absolute path** in your reply, on its own line, never shortened with `…`.
- First run only: if it fails with `Cannot find package 'playwright-core'`, do the one-time install in Step 1.

## Intent → flags

| What the user said | Flags |
|--------------------|-------|
| "the page", "the whole page", "full page" | `--full-page` |
| "this page" / no target / "what's on screen" | *(no target → viewport)* |
| "the pricing section", "the FAQ", "the hero" (named area) | `--section "pricing"` (heading match → enclosing `<section>`) |
| "the CTA button", "the nav", "`.hero`", "#footer" (one element) | `--selector ".hero"` |
| "the third section", "section 2" | `--section 3` |
| "the X inside the Y" | `--section "X" --container ".Y"` |
| "mobile view" / "on a phone" | `--device mobile` (390 × 844) |
| "tablet" / "desktop" | `--device tablet` / `--device desktop` |
| "at 1x" / smaller file | `--scale 1` (default is 2) |
| custom size | `--width 1440 --height 900` |
| "it loads slowly" / "wait for X" | `--wait 1500` or `--wait "<selector>"` |
| logged-in page | `--cdp <wsUrl>` (see Example 4) |

When unsure between a *named area* and an *exact element*, try `--section "<text>"` first (it falls back through heading → text → block). Use `--selector` when the user names a CSS selector or one small control.

## Workflow

```
- [ ] Step 1: Install deps (first run only)
- [ ] Step 2: Work out the URL and map the request to flags
- [ ] Step 3: Run scripts/screenshot.mjs
- [ ] Step 4: Open the printed PNG and report where it was saved
```

### Step 1: Install deps (first run only)

```bash
cd <skill-dir>/scripts && npm install
```

Installs `playwright-core` only. If neither Google Chrome nor a Playwright Chromium is on the machine, also run `npx playwright install chromium` in the same folder.

### Step 2: URL and target

- **URL**: a bare path like `/pricing` means the project's local dev server. Find its port from the project's dev script or the running process (`lsof -iTCP -sTCP:LISTEN` or `ss -ltn`), and start it if it isn't running.
- A local HTML file works too: `--url "file:///absolute/path/index.html"`.
- **Target**: map the user's phrasing with the table above.

### Step 3: Run the script

```bash
node <skill-dir>/scripts/screenshot.mjs --url "<url>" [target flags] [render flags]
```

The full option list is in the header of `scripts/screenshot.mjs`. Quick reference:

| Flag | Purpose | Default |
|------|---------|---------|
| `--url <url>` | Page to load (required) | — |
| `--full-page` | Whole scrollable page | off |
| `--selector <css>` | One exact element | — |
| `--section <value>` | Heading text, CSS, or Nth `<section>` | — |
| `--container <css>` | Ancestor to capture when matching by heading | nearest `<section>` |
| `--device <name>` | `mobile` \| `tablet` \| `desktop` preset | — |
| `--width / --height` | Viewport size | 1280 × 800 |
| `--scale <n>` | Device scale factor | 2 |
| `--wait <ms\|selector>` | Extra wait before capture | none |
| `--pad <px>` | Padding around a section/element clip | 0 |
| `--out <path>` | Output PNG path | timestamped file in the temp dir |
| `--cdp <wsUrl>` | Attach to a running Chrome (reuses its login) | launches a fresh one |
| `--headed` | Show the browser window | headless |
| `--channel <name>` | `chrome` \| `msedge` \| `chromium` | chrome, then chromium |

### Step 4: View and report

Open the PNG from the last stdout line to check it, then give the user the full absolute path. Pass `--out <path>` when the user wants it somewhere specific (a `screenshots/` folder in the project is a good default for before/after pairs). For several targets (mobile + desktop, three sections), run the script once per target.

## Examples

### Example 1: Whole page
**User:** "Screenshot example.com"
`node <skill-dir>/scripts/screenshot.mjs --url "https://example.com" --full-page`

### Example 2: A named section on the local app
**User:** "Screenshot the pricing section of /pricing"
`node <skill-dir>/scripts/screenshot.mjs --url "http://localhost:3000/pricing" --section "pricing"`

### Example 3: One element, mobile rendering
**User:** "Show me the nav on mobile"
`node <skill-dir>/scripts/screenshot.mjs --url "http://localhost:3000" --selector "nav" --device mobile`

### Example 4: A logged-in page (reuse a running Chrome)
**User:** "Screenshot the dashboard sidebar, it needs me logged in"
1. Ask the user to start Chrome with remote debugging and log in:
   - macOS: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=9222`
   - Linux: `google-chrome --remote-debugging-port=9222`
   - Windows: `"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222`
2. Read `webSocketDebuggerUrl` from `http://localhost:9222/json/version`.
3. `node <skill-dir>/scripts/screenshot.mjs --url "http://localhost:3000/dashboard" --selector "aside" --cdp "ws://localhost:9222/devtools/browser/XXXX"`

## Troubleshooting

**`Cannot find package 'playwright-core'`**: first run. `cd <skill-dir>/scripts && npm install`.

**`Failed to launch a browser`**: no Chrome and no Playwright Chromium. Install Google Chrome, or run `npx playwright install chromium` in `<skill-dir>/scripts`.

**`Could not find anything matching "X"`**: no heading or text matched. Pass an exact `--selector "<css>"`, or `--section <N>` for the Nth `<section>`. Take a `--full-page` shot first to pick a selector.

**Blank capture or missing late content**: the content rendered after `networkidle` or lazy-loads on scroll. Add `--wait 1500` or `--wait "<selector>"`. Sections are scrolled into view before capture, which triggers most lazy loads.
