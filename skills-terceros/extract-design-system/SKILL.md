---
name: extract-design-system
description: Reads a live URL or the current codebase and writes a DESIGN.md — color, typography, spacing, radius and shadow tokens, component patterns (buttons, cards, inputs, sections) and concrete do/don't rules — so every later agent run builds on-brand instead of inventing styles. Measures what the page actually renders with headless Chrome (computed styles, not guesses) and cross-checks the code's theme files. Use when the user says "extract the design system", "write a DESIGN.md", "pull the tokens from <url>", "document our styles", "capture our brand for the agent", "make the AI stop going off-brand", or "use <site>'s design system as a starting point". With the Landingfolio MCP connected it can also start from a page on landingfolio.com, or suggest a starting system from real category-matched pages when a project has none. Works without the MCP for any URL or codebase.
---

# Extract Design System

Turns a site or a codebase into one `DESIGN.md` that an agent can follow: real token values, how the components look, and rules specific enough to say no to ("one solid button per view", not "keep it consistent").

`<skill-dir>` below means the folder this SKILL.md is in (for example `.claude/skills/extract-design-system` or `~/.codex/skills/extract-design-system`).

## When to use this skill

- "Extract the design system from https://…" / "pull the tokens off our site"
- "Write a DESIGN.md for this repo" / "document our styles for the agent"
- "Our AI-built pages keep going off-brand" → this file fixes that at the source
- "Use <site>'s look as a starting point for my project"
- Before `explore-landing-sections` or `landing-page-audit`, when the project has no design doc yet (both read `DESIGN.md`)

## When NOT to use this skill

- The user wants the page restyled, not documented → do the restyle (read an existing `DESIGN.md` first)
- A design critique → `landing-page-audit`
- Copying another company's brand wholesale for a live product → extract the *system* (scale, spacing, component shapes) and tell the user to swap in their own colors, logo and fonts

## Connect the Landingfolio MCP

Optional here. Every URL and codebase extraction works without it. It adds two things:

- **Start from a Landingfolio page:** "use wispr-flow's style" → `get_inspiration_page` returns that page's screenshot tiles and colors, so you can extract from it even when the live site has changed or blocks headless browsers.
- **No system yet:** for a new project with nothing to extract, `get_components` with `category=hero` returns real live heroes; the user picks one or two they like and the starting system is extracted from those.

**Check first:** look for tools from a server named `landingfolio` (`list_categories`, `get_components`, `get_inspiration_page`; Claude Code shows them as `mcp__landingfolio__*`).

**If they're missing** and the task needs them, say so in one line and fall back (a plain URL extraction, or a starting system from the neutral defaults in Step 4b). Never block on it:

> The Landingfolio MCP isn't connected, so I can't pull real pages from landingfolio.com. To use them, get a free token at https://www.landingfolio.com/mcp and run:
> `claude mcp add --transport http landingfolio https://mcp.landingfolio.com/mcp --header "Authorization: Bearer <your-token>"`
> (Cursor, Codex, Windsurf, VS Code and others: the same page has the snippet for each.)

## Workflow

```
- [ ] Step 1: Pick the source (URL, codebase, both, Landingfolio page, or nothing yet)
- [ ] Step 2: Measure the rendered page (URL)
- [ ] Step 3: Read the code's theme (codebase)
- [ ] Step 4: Name the tokens by role
- [ ] Step 5: Describe the components and sections
- [ ] Step 6: Write the do/don't rules
- [ ] Step 7: Write DESIGN.md, check it, report
```

### Step 1: Pick the source

| Input | Do |
|-------|----|
| A URL | Step 2. If the URL is the user's own site and its repo is open, also Step 3: the code has the token *names*, the page has the *values in use*. |
| "This repo" / no URL, inside a project | Step 3. If a dev server runs or the site is live, also Step 2 on its homepage. |
| A landingfolio.com page or "like <site>" (MCP) | `get_inspiration_page` with the slug (from `landingfolio.com/inspiration/post/<slug>`). Use its colors and tiles; also run Step 2 on the live site if it's reachable. |
| A new project with nothing to extract | Step 4b. |

If a `DESIGN.md` already exists, read it first and update it in place; keep what the user wrote by hand unless the code contradicts it.

### Step 2: Measure the rendered page

```bash
node <skill-dir>/scripts/extract-url.mjs --url <url> --out-dir .design-extract
```

First run only: if it fails with `Cannot find package 'playwright-core'`, run `cd <skill-dir>/scripts && npm install` (installs `playwright-core` only; it drives the installed Google Chrome). If no Chrome is installed, also run `npx playwright install chromium` there. If you can't run Node, fetch the HTML and its CSS files and read the values by hand.

It prints a summary and writes `.design-extract/tokens.json` plus `desktop.png`, `desktop-full.png` and `mobile.png`. The summary has, from the browser's computed styles:

- text, background and border colors ranked by how much they're used (text by characters, backgrounds by area)
- font families, the fonts that actually loaded, and the size / line-height / weight / tracking of h1–h6, body and small text
- padding/margin and gap values by frequency (the spacing scale), radii, shadows
- button variants (background, text, radius, height, border) with their labels
- top-level sections with background and vertical padding
- `:root` custom properties (the site's own token names, if it has any)

**Open the screenshots.** Numbers don't say which color is the brand accent or how the hero is composed; the screenshots do. A color used on 3 elements can still be the primary if it's on every CTA.

If the page needs a login, ask for a public page or a screenshot. A screenshot alone works too: estimate values from it and mark them *(inferred)*.

### Step 3: Read the code's theme

```bash
bash <skill-dir>/scripts/scan-codebase.sh <repo-root>
```

It lists existing design docs, the framework, Tailwind v3 configs and v4 `@theme` blocks, CSS files with custom properties, token files, how fonts load, the shared UI component folders, and the most-used Tailwind color/radius/shadow classes. Then read:

1. The theme source (the `@theme`/`:root` file, `tailwind.config.*`, or the tokens file). Record token **names and values** as written.
2. The shared `Button`, `Card`, `Input` and `Badge` components: variants, sizes, states.
3. Two or three real pages (the homepage, a pricing or feature page) to see how sections are put together.

Where the theme defines tokens nobody uses and pages use raw values instead (`text-gray-500` all over, `#7c3aed` hard-coded), say so in the doc: the rule is what's in use, plus a note to migrate.

### Step 4: Name the tokens by role

Map raw values to roles; [references/reading-tokens.md](references/reading-tokens.md) has the heuristics (which background is the page vs a surface, how to find the primary, collapsing near-duplicate greys into a scale, rem vs px, what to do with one-offs). In short:

- **Color:** background, surface, ink, ink-muted, ink-subtle, border, primary (+ foreground), accent, status colors only if present. Use the code's token names when they exist.
- **Type:** font per role, the type scale (display → caption) with size / line-height / weight / tracking, and the mobile H1 size from `mobile.png`.
- **Spacing:** the base unit and the scale actually used (most pages land on 4/8-based steps), section padding desktop vs mobile, content max-width.
- **Radius, shadows:** 3–5 steps each, with what uses them.

Every value comes from a measurement or a file. If you had to guess, write *(inferred)* after it.

### Step 4b: No system to extract (starting from scratch)

- **MCP path:** ask what the product is and its tone in one line if you don't know. `list_categories`, then `get_components` with `category=hero` (and `pricing` or `feature` if useful). Download and open the screenshots (`curl -sL "<image-url>" -o .design-extract/refs/<n>.jpg`), shortlist 3–4 that fit, and let the user pick 1–2 (in a non-interactive run, pick the closest fit and say why). Extract the *system* from the pick: palette structure (neutral paper + one accent? dark?), type pairing and scale, density, radius personality, button style. Never copy their logo, brand colors exactly, or copy.
- **No-MCP path:** start from neutral defaults (off-white background, near-black ink, one accent the user chooses, a 4px spacing grid, Inter or the system stack, radius 8/12/16) and mark the whole doc as a starting point to revise.

### Step 5: Describe the components and sections

From the screenshots and the component code, fill in buttons (each variant with its colors, radius, height, padding, weight, and states if visible in code), cards, inputs, badges, and **section patterns**: how a section header is built (eyebrow + H2 + subhead? centered?), alternating backgrounds or not, what the hero, logo row, pricing and footer look like. A sentence per pattern is enough; the agent needs to be able to build a new section that sits next to the old ones.

### Step 6: Write the do/don't rules

5–10 rules total, each checkable in a code review and grounded in something you measured. Good rules name values:

- ✅ "Exactly one solid `primary` button per view; secondary actions are outline (`border` + `ink`)."
- ✅ "Body text is `ink-muted` (#78716c) at 15px/1.6; never pure black."
- ✅ "Cards: 1px `border`, radius 12px, no shadow. Only floating UI (menus, popovers) gets a shadow."
- ❌ "Keep it clean and consistent." (not checkable)
- ❌ "Use modern design." (not a rule)

Don'ts come from what the system visibly avoids (no gradients anywhere? no all-caps headings? no second accent?) and from drift you found in Step 3.

### Step 7: Write, check, report

Copy `<skill-dir>/assets/DESIGN.template.md` to `DESIGN.md` at the project root (or where the user asked) and fill every section; delete rows that don't apply rather than leaving placeholders. Keep it under ~200 lines: tables for tokens, short sentences for patterns.

Check before reporting:

- No `{{…}}` placeholders left: `grep -n "{{" DESIGN.md` prints nothing.
- Spot-check three values against the source (a color, the H1 size, the primary button radius).
- If the project has an agent instructions file (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `GEMINI.md`), offer to add one line pointing at `DESIGN.md`. Don't edit it without asking.
- `.design-extract/` is scratch: tell the user they can delete it, or add it to `.gitignore`.

Report: the file path, the brand in one line, the primary/accent colors and fonts, how many tokens came from code vs measured vs inferred, and which path ran (URL / codebase / Landingfolio page / starting point; MCP or not).

## Examples

**"Extract the design system from https://acme.dev"** → `extract-url.mjs` → open screenshots → primary is the violet on every CTA (#6d28d9, ×4) even though grey dominates by count → type: Inter Display 56/60 w600 H1, 16/26 body → spacing on an 8px grid, sections 96px desktop / 56px mobile → buttons: solid violet, outline, ghost → rules → `DESIGN.md`.

**"Write a DESIGN.md for this repo"** (Next + Tailwind v4) → `scan-codebase.sh` → `@theme` in `app/globals.css` has 40 tokens → read `components/ui/button.tsx` and `card.tsx` → the dev server is running, so `extract-url.mjs --url http://localhost:3000` confirms what renders → note that pages use `text-gray-500` instead of the `muted-foreground` token → `DESIGN.md` with token names from code.

**"Start my design system from wispr-flow on Landingfolio"** → `get_inspiration_page slug=wispr-flow` → colors + tiles → `extract-url.mjs` on the live site for exact type and spacing → `DESIGN.md` with "Started from wispr-flow's system; swap in your own accent and logo."

**New project, no MCP** → one-line connect note → neutral defaults with the user's accent → `DESIGN.md` marked as a starting point.

## Troubleshooting

- **`Cannot find package 'playwright-core'`:** `cd <skill-dir>/scripts && npm install`.
- **`Failed to launch a browser`:** install Google Chrome, or `npx playwright install chromium` in `<skill-dir>/scripts`.
- **Cookie banner or modal covers the screenshots:** values are still measured from the whole page; mention it, or pass `--wait 3000` if content loads late.
- **Page blocks headless browsers (403, captcha):** ask for a screenshot, or use `get_inspiration_page` if the site is on Landingfolio.
- **Dozens of greys:** collapse near-duplicates into a 3–5 step neutral scale and note the strays as drift.
- **Fonts show as a fallback (Arial, Times):** the webfont didn't load; check `loadedFonts` in `tokens.json` and the code's font imports.
- **Rate limit (429) from the MCP:** the free tier is 100 requests a day; one `get_components` call is enough here.
