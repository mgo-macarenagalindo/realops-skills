# Implementing the chosen direction

**Contents:** When to run · Critical rules · Workflow (1 extract reference · 2 content inventory · 3 resolve gaps · 4 build · 5 parity loop · 6 mobile check) · Examples · Troubleshooting

Turns the picked direction into the real section in the user's codebase, and keeps going until it looks like the mock, on desktop and on a phone.

The recurring failure this phase prevents: the mock looked great because it was drawn with perfect content (six testimonials with photos, a crisp product shot, a metric on every card); the build comes out barebones because missing content gets silently dropped and hand-tuned proportions shrink in translation. Here every content gap becomes an explicit decision and every proportion is diffed against the reference.

## When to run

- "Go with B" / "implement option C" / "build this direction"
- "B, but with A's logo row" (a mix: extract both parts in Step 1)
- "The build doesn't look like the mock" (jump to Step 5)

## Critical rules

- **Never silently hide a missing element.** Every element of the mock without real content behind it gets a decision in Step 3.
- **Done = visual parity, not "it renders".** Diff screenshots against the reference until the delta list is empty or each remaining delta is a deliberate, written-down choice.
- **Match proportions, not just presence.** Type size and weight, spacing rhythm, image scale, radius, accent placement. Reproducing the right elements at smaller, thinner sizes is how builds end up looking cheaper than mocks.
- **Build in the project's conventions**, not the mock's vanilla CSS: its framework, components, tokens and class naming.

## Workflow

Post a one-line status when entering each step ("inventory: 2 gaps", "parity round 2: hero image too small, CTA weight").

```
- [ ] Step 1: Extract the picked direction to a standalone reference file
- [ ] Step 2: Content inventory: what's real, what's missing
- [ ] Step 3: Resolve every gap (with the user when reachable)
- [ ] Step 4: Build it in the real codebase
- [ ] Step 5: Parity loop: reference vs build, explicit delta list
- [ ] Step 6: Check the 390px mobile layout
```

### Step 1: Extract the reference

Copy the picked direction's markup **and** its scoped CSS (plus the brand `:root` tokens it uses) into its own file that renders standalone:

```
design-explorations/<section>-<short-name>-<letter>.reference.html
```

This is the single source of truth for parity. Diffing against one panel of a 4-up page is error-prone. Confirm the pick in one line ("Building C, proof-first pricing").

### Step 2: Content inventory

Walk every element of the reference and classify where its content comes from:

| Class | Meaning |
|-------|---------|
| ✅ **Real** | Exists in the codebase/CMS today (headline, plan prices, the 3 testimonials in `testimonials.json`) |
| ⚠️ **Partial** | Exists but thinner than the mock (2 testimonials, the mock shows 6; quotes without photos) — quantify it |
| ❌ **Invented** | Drawn in the mock, doesn't exist (customer logos, a "4,000 teams" metric, a product screenshot of a feature not built) |

Write it to `<...>-<letter>.inventory.md` next to the reference: element → source → class → decision (filled in Step 3).

Invented **numbers, quotes, customer names and logos** never ship as if real. They are always a gap.

### Step 3: Resolve every gap

For each ⚠️ and ❌ element pick one, and recommend the option that makes the element work with the content the user actually has:

- **Source it** — the user provides it (real logos, a testimonial, a screenshot). Ask where it lives.
- **Derive it** — build it from what exists (initials avatars from names, a stat computed from real data, a product shot taken with a screenshot tool).
- **Designed placeholder** — an intentional, composed state with a clear `TODO` the user can find (never a grey box).
- **Cut it** — drop the element on purpose and rebalance the layout so it doesn't leave a hole.

If the user is reachable, batch all gaps into one question. If not (a non-interactive run), choose Derive or Cut, never invent content, and list each decision in the report. Record decisions in the inventory. Don't start building until every gap has one.

### Step 4: Build

Read the project's own docs first (`CLAUDE.md`, `AGENTS.md`, contributor docs, `DESIGN.md`, and `design-explorations/_brand.md` for the design-system path). Then:

- Reuse the project's components (buttons, cards, section wrappers) and tokens (theme colors, fonts, spacing scale); map the mock's values onto the nearest tokens instead of hard-coding hex values.
- Keep existing test ids, analytics hooks, links and behavior of the section you're replacing.
- Apply the Step 3 decisions.
- Reproduce the reference's proportions: the heading's size and weight, the gap rhythm, image size and crop, radius, where the accent color goes.

### Step 5: Parity loop

Screenshot the reference file and the built section at the same width (1280px) — with a screenshot skill such as `screenshot-capture`, a browser MCP, or Playwright; ask the user for screenshots only as a last resort. Open both images and write down **every** delta:

- Presence — element in one, not the other
- Size — type, images, cards, buttons
- Weight — headline and number boldness
- Spacing — padding, gaps, vertical rhythm
- Color, radius, borders, shadows

Fix and repeat until the list is empty, or each remaining delta is a deliberate deviation written in the inventory ("kept the project's 8px radius instead of the mock's 12px"). One screenshot that "looks fine" is not the loop.

### Step 6: Mobile

Screenshot the built section at 390px wide. Check: no horizontal scroll, headline doesn't break into one word per line, CTAs are full-width or comfortably tappable, rows of 3+ peer cards don't become an endless stack (a swipe row or 2-column grid often reads better). Fix what's off.

Report: the reference and inventory paths, the gap decisions, the desktop and mobile screenshots, and any deliberate deviations.

## Examples

**"Go with C"** (proof-first pricing) → extract C → inventory: plans ✅, 3 testimonials ⚠️ (mock shows 6, no photos), "Trusted by 4,000 teams" ❌ → user: use the 3 real quotes with initials avatars, cut the metric → build with the project's `Card` and `Button` → parity round 1: plan names too small, highlighted-plan ring missing → round 2: clean → 390px: plans stack, testimonials become a swipe row → report.

**Non-interactive run** → same, but gaps resolved as Derive/Cut without inventing anything, and listed in the report for the user to revisit.

## Troubleshooting

- **The build looks cheaper than the mock:** proportion drift. Run Step 5 properly with a written delta list on size, weight and spacing.
- **The section looks empty:** a gap was silently hidden. Back to Step 3 for that element.
- **Mock styles fight the project's styles:** you pasted the mock's CSS. Rebuild with the project's components and tokens, using the mock as a visual target only.
