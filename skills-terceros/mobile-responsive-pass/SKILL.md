---
name: mobile-responsive-pass
description: Makes an existing desktop-first landing page or marketing page feel intentional on a 375–390px phone in one pass, without touching the desktop design. Use when the user asks to "make this mobile friendly", "optimize for mobile", "fix the mobile layout", "make it more compact on mobile", "reduce scrolling on mobile", or hands over a page that looks fine on desktop but cramped or endless on a phone. Tactical, not a redesign: shrinks padding, type and gaps; restructures layouts that physically can't fit (wide tables, chip rows, big grids); flattens double-padded cards; and on marketing pages turns tall stacks of peer cards (pricing tiers, testimonials, steps, galleries) into swipe carousels. Works on plain HTML/CSS, Tailwind, and any component framework (React, Vue, Svelte, Astro).
---

# Mobile Responsive Pass

Take a desktop-first page and make it feel designed for a phone, without changing how it looks on desktop.

This is **not a redesign**. Desktop-first pages break on mobile in the same handful of ways: oversized vertical padding, desktop-size headings, wide card padding, big grid gaps, small CTAs, one or two layouts that physically can't fit (a 3-column comparison table, a wide chip row), and on marketing pages, rows of peer cards that stack six deep. This pass fixes those, consistently, across every section.

Code for every pattern below is in [references/patterns.md](references/patterns.md), each shown in **plain HTML/CSS** and **Tailwind**. Read it before editing.

## Step 0: Detect the styling approach

Look at the files before changing anything. Each approach has its own way to say "mobile value, then the original desktop value":

| The page uses | Mobile-only change looks like |
|---|---|
| **Tailwind** (`class="py-24 text-4xl"`) | `py-12 sm:py-24`: the unprefixed class is mobile, `sm:` restores desktop |
| **Plain CSS / SCSS / CSS modules** | Keep the desktop rule as is; add overrides inside `@media (max-width: 639px) { … }` |
| **CSS-in-JS / styled-components** | Same media query inside the component's styles |
| **A design-system component library** | Check what the primitives already do on mobile before overriding (see below) |

Pick **one breakpoint** for the whole pass and use it everywhere. The default is 640px (Tailwind's `sm`); if the project already has a mobile breakpoint in use (`$mobile`, `768px`, `md`), use that one instead.

The framework (React, Vue, Svelte, Astro, plain HTML) doesn't change the technique. Edit the markup and classes or styles; leave component logic alone.

## Workflow

1. **Read every section the page renders.** A landing page is usually one file that mounts 8–15 section components or partials. Open each one; you can't fix mobile from the parent.
2. **Check what is already handled.** Grep for existing media queries, `clamp(`, and shared section/card wrappers. If a shared `Section` wrapper already drops padding on mobile, don't add more on top. If headings use `clamp()`, read **Clamp floors** below before skipping them.
3. **Look at the real render, one section at a time.** If a dev server is running, capture each section at 390px wide (`screenshot-capture` skill: `--device mobile --section "<heading>"`, or any headless browser). Don't judge from a single full-page mobile capture; it shrinks to an unreadable sliver.
4. **Apply the mobile-down scale** (below) uniformly: same breakpoint, same numbers, same patterns in every section. Consistency is what makes the page feel intentional instead of patched.
5. **Flatten double-padded cards and drop dead backgrounds.** Usually the biggest single win. See **Don't double-pad**.
6. **Size down headings that wrap badly** with a mobile-only override on that one heading.
7. **Restructure anything that physically can't fit**: wide tables, flex-wrapped chip rows, dense hero grids. These need a mobile-specific layout, not smaller text.
8. **Carousel tall rows of peer cards** on marketing pages (tiers, testimonials, steps, galleries, cross-link cards). This is part of the default pass, not something to wait for.
9. **Fix tap targets and CTAs**: primary buttons full width, 44px minimum tap height.
10. **Verify desktop is untouched** and re-capture each changed section at 390px.

## The mobile-down scale

Use these numbers everywhere. Left is a typical desktop value, right is what it becomes (mobile value → desktop value restored at the breakpoint). Pixel values are given so they work in plain CSS too.

| Thing | Desktop | Mobile |
|---|---|---|
| Section vertical padding | 64–96px | 48px |
| Section header margin below | 48px | 32px |
| H1 (hero) | 36–56px | 28–32px, line-height 1.15 |
| H2 (section heading) | 30–40px | 26px, line-height 1.2 |
| Body copy | 18px | 16px |
| Dense card body | 16px | 14px |
| Eyebrow / uppercase label | 12px | 11px |
| Card padding | 32px | 20px |
| Card padding (already 24px) | 24px | 20px |
| Grid gap (large) | 56–80px | 32px |
| Grid gap (medium) | 40px | 32px |
| Grid gap (small) | 24px | 16px |
| Flex gap inside a card or hero column | 32px / 16px | 20px / 12px |
| Decorative icon tile | 48px | 40px |
| Decorative step numeral | 56px | 40px |
| Horizontal page gutter | 24–32px | 16–20px |

Anything purely decorative (icons, numerals, badges, illustrations) shrinks proportionally. Anything carrying information (prices, labels a user must read) does not go below 14px.

## Don't double-pad: drop the background, flatten the card

The most common source of cramped mobile text is a **padded card sitting inside a padded section on top of a decorative background**: a hero or CTA where a gradient, blob, or image wall fills the section and a white card floats over it with its own border, shadow and padding.

On a phone that stack works against you:

- The **background does nothing**: the card fills the width, so the decoration behind it is a thin sliver.
- The card carries **its own padding** on top of the section's: 24px + 24px per side leaves a ~280px text column on a 375px screen. Its border and shadow only exist to lift it off a background you can no longer see.

**Remove a layer, don't shrink it.** On mobile, hide the decorative background, and drop the card's border, shadow, blur, background and padding so the content sits in a single layer of section padding at full width. Restore all of it at the breakpoint.

Rule of thumb: if a wrapper's only job is to be a visual container over a background, and that background is gone on mobile, the wrapper adds **zero** padding on mobile.

## Clamp floors aren't free

Fluid headings like `font-size: clamp(28px, 5vw, 56px)` stop shrinking at their floor. Below ~560px every phone gets the 28px floor, and a long heading at that size can still wrap to three ragged lines and eat the first screen.

When a real render shows a heading wrapping badly, size **that heading** down one notch on mobile only (28px → 24px usually turns three lines into two) and tighten its line-height. **Don't edit the shared token or the global `h1`/`h2` rule** during this pass; that reflows every page. If the floor looks wrong everywhere, tell the user it's a separate token change.

## Restructure what can't fit

These layouts can't survive 375px however small the text gets. Swap them (code in the patterns file):

- **3-column comparison table → stacked cards.** Hide the table on mobile; render one card per row with "us" and "them" side by side in a 2-column mini-grid.
- **Wrapped chip or filter row → one horizontal scrolling row** that bleeds to the screen edge, chips don't shrink.
- **6-tile hero grid: 2 columns → 3 columns on mobile.** Counterintuitive but correct: 2 rows of 3 is less scroll than 3 rows of 2.
- **Long button or ribbon labels → a short mobile label and the long one on desktop**, as two spans toggled by the breakpoint. Never truncate with an ellipsis.

## Carousels: the default for landing-page card rows

On a marketing or landing page, a row of 3–7 peer cards that stacks to one column on mobile (pricing tiers, testimonials, steps, gallery items, "related" cards) is the biggest source of mobile scroll. Turn it into a horizontal swipe row by default.

Always:

- **Peek the next card**: each card ~80–85% of the width, so it's obvious the row swipes.
- **Snap**: `scroll-snap-type: x mandatory` on the track, `scroll-snap-align: start` on cards.
- **Bleed to the screen edge**: negative margin equal to the page gutter, matching padding inside.
- **Dots** on the high-stakes rows (pricing especially) so people know more tiers exist.
- **Hide the scrollbar** with `scrollbar-width: none` and `::-webkit-scrollbar { display: none }`.
- Mobile only: the desktop grid comes back at the breakpoint.

Don't carousel:

- Content inside a **logged-in app** (dashboards, settings, data tables, forms): keep native vertical scroll there.
- **Trust or safety commitments** you want fully visible, and **comparison ledgers** that read better vertically.

Gotchas:

- `overflow-x: auto` also clips vertically. A "Most popular" badge sitting above a card, or a card's drop shadow, gets cut off. Give the track vertical padding on mobile.
- Flex rows stretch cards to the tallest one. Keep line clamps so one long testimonial doesn't make every card tall.
- If you wrap an existing block in a new element, change the opening **and** closing tag in the same edit, then re-read the closing region.
- A card with its own horizontal drag control (range slider, before/after slider) can fight the swipe. If that control dominates the card, leave the row stacked and say so.

## Tap targets and CTAs

- **Primary CTAs go full width on mobile** (`width: 100%`, back to auto at the breakpoint). In a stacked pair of CTAs, the secondary button gets the same treatment.
- **Flex columns holding CTAs stretch** on mobile (`align-items: stretch`) so the buttons line up edge to edge.
- **Minimum tap height 44px** for buttons and text-link CTAs.
- **Nav**: if the desktop nav links wrap or overflow at 390px, collapse them behind a menu button or keep only the primary CTA visible. Don't let the header wrap to two lines.

## What not to touch

- **Desktop values.** Every change is "mobile value, desktop restored at the breakpoint". If you change a desktop value or reach for a larger breakpoint, you're redesigning.
- **Component logic**: no prop, state or behavior changes. Markup and styles only.
- **Copy**, except the paired short/long labels for strings that can't fit.
- **Colors, brand, imagery choices.**
- **Section order and content.** Mobile shows the same sections and content as desktop. Carouseling a card row is a layout change and is fine; removing sections or trimming proof is not, unless the user explicitly asks for a shorter page.
- **Shared tokens and global type rules.** Override on the instance.

## Verification checklist

- [ ] One breakpoint used consistently across every section
- [ ] Section vertical padding ≤ 48px on mobile (or the shared wrapper already handles it)
- [ ] Section headings 26px on mobile; any heading that wrapped to 3 lines at 390px now wraps to 2, via an instance override
- [ ] No card padding above 20px on mobile
- [ ] No double padding: where a card floats on a decorative background, the background is hidden and the card adds no padding or chrome on mobile
- [ ] Every primary CTA is full width on mobile with a ≥44px tap height
- [ ] Any 3-column table has a mobile card fallback
- [ ] Chip rows scroll horizontally on mobile (or fit on one row)
- [ ] Peer-card rows on a marketing page are swipe carousels with peek, snap, edge bleed, and dots on pricing; nothing carouseled in app UI
- [ ] No horizontal scroll on the page itself at 390px (`document.documentElement.scrollWidth <= 390`)
- [ ] Each changed section re-captured at 390px and checked
- [ ] Desktop unchanged: a desktop capture before and after looks the same

## Report

When done, give the user a per-section list in this shape:

> - **Hero**: dropped the background blob and card chrome on mobile, H1 32px → 28px
> - **Pricing**: 3 stacked tiers → swipe carousel with dots

No prose; they review the diff against this list.
