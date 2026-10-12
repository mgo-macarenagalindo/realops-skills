---
name: explore-landing-sections
description: Explores 3–6 distinct directions for one landing-page section (hero, pricing, testimonials, features, CTA, FAQ, logos, footer…) on a single side-by-side HTML comparison page, grounded in real live examples pulled from Landingfolio's gallery through the Landingfolio MCP, then implements the direction the user picks in their real codebase. Use when the user says "explore directions for the hero", "show me a few pricing section options", "give me some ideas for this section", "what could our testimonials look like", "concept the CTA", "redesign this section", or wants to compare section layouts before committing. Also handles the follow-up — "go with B", "implement option C", "build this direction" — via references/implement.md. Works without the MCP too, using the section-pattern catalog in references/section-patterns.md.
---

# Explore Landing Sections

Produces ONE standalone `.html` file that shows several directions for one landing-page section side by side, each one grounded in real sections from live landing pages, so the user picks on a visible tradeoff instead of a vibe. Then builds the pick for real.

Two phases:
1. **Explore** (this file): pull real examples, write the comparison page.
2. **Implement**: when the user picks a direction, read [references/implement.md](references/implement.md) and follow it.

`<skill-dir>` below means the folder this SKILL.md is in (for example `.claude/skills/explore-landing-sections` or `~/.codex/skills/explore-landing-sections`).

## When to use this skill

- "Explore directions for the hero / pricing / testimonials section"
- "Show me 4 options for this section" / "brainstorm the CTA" / "what could the FAQ look like"
- "Redesign the features section, but show me options first"
- "Go with B" / "implement option C" / "build this direction" (→ implement phase)
- "Init" / "rebrand the explorations" (→ re-run brand init, [references/brand-init.md](references/brand-init.md))

## When NOT to use this skill

- The user wants a whole page built straight away with no comparison step → build it directly
- A small tweak to a shipped section (padding, one color, a copy change) → just edit it
- A critique of an existing page → use a design audit (e.g. the `landing-page-audit` skill)

## Connect the Landingfolio MCP

The MCP is what grounds each direction in real, current, category-matched sections from landingfolio.com instead of the model's memory of "what a hero looks like". It's free (100 requests a day).

**Check first:** look for tools from a server named `landingfolio` — `list_categories`, `get_components`, `pick_components`, `get_components_by_id`, `get_inspiration_page` (Claude Code shows them as `mcp__landingfolio__*`).

**If they're missing**, tell the user in one line and keep going on the no-MCP path below. Never block on it:

> Landingfolio MCP isn't connected, so these directions come from the built-in pattern catalog instead of live examples. To ground them in real sections, get a free token at https://www.landingfolio.com/mcp and run:
> `claude mcp add --transport http landingfolio https://mcp.landingfolio.com/mcp --header "Authorization: Bearer <your-token>"`
> (Cursor, Codex, Windsurf, VS Code and others: the same page has the snippet for each.) Restart the agent after adding it.

## Workflow

Narrate as you go: one status line after the scan, after the examples are in, before writing (the theses), and after writing (the path). The writing stretch runs minutes; silence must never be the first sign of progress.

```
- [ ] Step 1: Brand scan (init gate)
- [ ] Step 2: Scope to one section and read its real content
- [ ] Step 3: Pull real examples (MCP) — or the pattern catalog (no MCP)
- [ ] Step 4: Announce 3–6 distinct theses
- [ ] Step 5: Write the comparison page from the template
- [ ] Step 6: Open it, check it, report
- [ ] Step 7: On a pick → references/implement.md
```

### Step 1: Brand scan — always first

```bash
bash <skill-dir>/scripts/scan-brand.sh <repo-root>
```

- `STATUS: TEMPLATE_FOUND` → reuse the repo's branded template; say so, continue.
- `STATUS: NO_TEMPLATE` → read [references/brand-init.md](references/brand-init.md) and finish brand init **before** writing any exploration HTML. It ends with `design-explorations/_template.html` and `_brand.md` on disk. If the scan lists a `DESIGN.md` (for example one written by the `extract-design-system` skill), that is the brand source of truth.

### Step 2: Scope and read the real content

Name the **one** section being explored and its category. Landingfolio's slugs include `hero`, `feature`, `pricing`, `testimonial`, `call-to-action`, `faq`, `logo-cloud`, `how-it-works`, `stats`, `integrations`, `team`, `contact`, `newsletter`, `header`, `footer` (`list_categories` has the live list). If the user asked about a whole page, pick the highest-leverage section (almost always the hero) and say what you scoped to.

Read the current section in the codebase (or the page's live HTML) and collect its **real content**: headline, subhead, CTAs, plan names and prices, testimonial quotes and names, logos, feature list. Every direction uses this same content. Lorem ipsum kills the exercise. If there's no existing section, read the README / other pages for the product and its audience; ask only if you still can't tell what the product is.

### Step 3a: Pull real examples (MCP path)

1. `list_categories` → find the slug that matches the section; use it exactly.
2. Get examples, one of two ways:
   - **Newest (default):** `get_components` with that category. 12 results per page; take page 2 as well if fewer than 8 fit the product.
   - **User picks by eye:** if the user wants to choose, or says "use the ones I like": `pick_components` (pass `industry`, e.g. `saas`, when you know it), share the link, wait for the code they paste back, then `get_components_by_id`. When the user is reachable and hasn't said, ask once which they prefer; in a non-interactive run use newest.
3. **Actually look at them.** Download each screenshot and open it — never pick from URLs alone:
   ```bash
   mkdir -p design-explorations/refs && curl -sL "<image-url>" -o design-explorations/refs/<site>-<n>.jpg
   ```
4. Keep the 6–10 that fit the product (audience, tone, content shape: a 3-tier pricing product needs 3-tier references). For each keeper, note in one line what it does structurally (e.g. "split hero, product UI bleeding off the right edge, logo row under the CTA"). Keep each one's `image` and `source` URL for the page.

### Step 3b: Pattern catalog (no-MCP path)

Read [references/section-patterns.md](references/section-patterns.md) for the section's category: the common structural patterns with what each optimizes for. If the user named sites or shared screenshots they like, those are the references; look at them the same way. Set the header's References meta to "Pattern catalog (Landingfolio MCP not connected)" and delete the `.variant-refs` strips unless user references exist.

### Step 4: Announce the theses

Brainstorm 4 directions (range 3–6), each with a one-sentence thesis, each traceable to 1–3 of the references from Step 3 ("C) proof-first: testimonial wall above the plans, after <site> and <site>"). **Post them before writing** — this is the last message before the longest silent stretch.

Distinct means different **structure, hierarchy, density, or what's prioritized** — never the same layout in different colors. If you can't write distinct one-sentence theses, you don't have distinct directions.

### Step 5: Write the comparison page

Copy `design-explorations/_template.html` to `design-explorations/<section>-<short-name>.html` and fill it in:

- **Header:** title ("Pricing section — four directions"), subtitle, the source file in Spec, date, the reference source in References ("12 live pricing sections from Landingfolio").
- **Per direction:** letter + name, the tradeoff line (what it optimizes for AND what it gives up), the **Grounded in** strip (1–3 references: screenshot thumbnail + site name, linking to the `source` URL), the live preview, and the three analysis blocks (≤ 3 sentences each).
- **Decision row:** "If you want X → pick A. If Y → pick B…"

Rules for the previews:

- Every direction wears the user's brand from init (fonts, colors, feel). Exploration happens in **layout, hierarchy, density and emphasis**. Go off-brand only when the user explicitly asks for visual-identity directions.
- **Borrow structure, never identity.** Take a reference's layout idea and level of polish; never its copy, logo, product shots, illustrations or brand colors. Hotlinked screenshots appear only in the Grounded-in strip, never inside a preview.
- Match the references' **level of design**: their accent use, badges, contrast between sections, type weight, button treatment. A grey-box wireframe is a failure.
- All directions use the same real content from Step 2.
- Previews render at desktop width; if the section's mobile layout differs meaningfully between directions, mention it in the analysis.
- One HTML file, vanilla CSS, no Tailwind CDN or JS frameworks. Scope each direction's CSS with a prefix (`.va-`, `.vb-`, …). System-font fallbacks on every font stack. No comments except the top-of-file header.

### Step 6: Open, check, report

Open the file (`open` on macOS, `xdg-open` on Linux, `start` on Windows; skip when headless). If you can take screenshots (a screenshot skill such as `screenshot-capture`, a browser MCP, or Playwright), capture the page and look at it: fix overlapping text, broken images, or directions that look alike before reporting.

Report: each direction with its one-line tradeoff and the references behind it, the file path, and which path ran (MCP with N examples, or pattern catalog). End with "Pick a letter and I'll build it."

### Step 7: Implement the pick

When the user picks ("go with C", "B but with A's logo row"), read [references/implement.md](references/implement.md) and follow it.

## Examples

**"Explore some directions for our pricing section"** → scan (template found) → `list_categories` → `get_components category=pricing` (12 results) → download and view them, keep 8 that suit a 3-tier SaaS → theses: A) toggle-led 3-tier with highlighted middle plan (after Linear, Vercel), B) single plan + comparison table, C) proof-first with testimonials above the plans, D) calculator-led → `design-explorations/pricing-four-directions.html` → open → report.

**Same request, no MCP** → one-line connect note → `references/section-patterns.md` → pricing patterns → same four theses from the catalog → page with References "Pattern catalog" and no Grounded-in strips.

**"Let me pick the examples"** → `pick_components category=hero industry=saas` → share the link → user pastes `acme:65f…  globex:65f…` → `get_components_by_id` → those become the references.

## Troubleshooting

- **Directions look alike:** the theses aren't distinct. Rewrite them before touching CSS; push on structure and priority, not color.
- **Previews look like wireframes:** you described the references instead of matching their level of design. Re-open the screenshots and copy their caliber of decisions (accent placement, contrast, weight).
- **`Unknown category`:** call `list_categories` and use a slug from it exactly.
- **A reference's brand leaked into a preview** (its colors, logo, headline): replace with the user's brand and content; references inform structure only.
- **Rate limit (429):** the free tier is 100 requests a day. Work with the examples you already have; don't page further.
- **Generated without brand init:** run the scan, finish init, re-skin the page from the branded template.
