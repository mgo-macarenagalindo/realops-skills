# Share image: design recipe

A share image (Open Graph / Twitter card) is the picture that shows up when a link is pasted into LinkedIn, X, Slack, iMessage, Discord or WhatsApp. It's seen small, next to other posts, for about a second. It works like a tiny billboard: one message, read at a glance.

The deliverable is a flat JPG rendered from a self-contained HTML canvas.

## Canvas

- **Logical size 1200 × 630** (1.91:1), the size every platform crops to. Author at this size.
- **Rendered at 2× → 2400 × 1260** for sharp text on retina screens. Use `--scale 1` if the file comes out over ~1 MB.
- The body is pinned to exactly the canvas with `overflow: hidden`. Anything outside is cropped.
- **Safe area**: keep text and the logo at least 64px from every edge. Some platforms crop a little off the sides (X shows ~1.91:1 but WhatsApp and iMessage can show a squarer crop, centered), so the headline should sit in the middle 1000px.

## Brand inputs

These come from the user (or from the project, confirmed by the user). Never borrow colors, logos or imagery from anywhere else.

| Input | Used for | If missing |
|---|---|---|
| Primary / accent color | eyebrow, one shape or underline, or the whole field on a bold card | ask; don't guess a "nice" color |
| Background color | the field | the brand's lightest neutral, or white |
| Text color | headline | near-black on light fields, near-white on dark |
| Logo file (SVG preferred, PNG ok) | top of the card, ~40px tall | a text wordmark in the brand font, product name only |
| Font | everything | the font the site uses; otherwise Inter |
| Product visual (optional) | split and peek layouts | use the centered layout instead |

**Contrast**: headline vs field must be at least 7:1 (it's read small). Muted text at least 4.5:1. If the brand's primary color fails as a field color behind dark text, use it as the field with white text, or keep it to the accent role.

**One field color.** A flat brand color or a flat neutral. No full-canvas gradients, no busy photos behind text.

## Typography

- **Headline**: 56–72px, weight 700–800, line height ~1.05, tight tracking (-0.02em). **One or two lines, never three.** If it wraps to three, shorten the copy first, then step the size down by 4px at a time, never below 52px.
- **Eyebrow** (optional): 16–18px, bold, uppercase, +0.08em tracking, accent color.
- **Subline / proof** (optional): 24–28px, weight 500, muted color. One line.
- **Logo**: ~40px tall. It's secondary; the headline is the loudest thing on the card.

## Copy

- The headline is the page's promise, not its name. "Landing page feedback in 5 minutes" beats "Acme: The Feedback Platform".
- Use the page's own H1 if it's short and concrete. Otherwise tighten it to ≤ 8 words. Don't invent claims the page doesn't make.
- The subline is a concrete proof point or a plain description. Real numbers only, and only if the page states them.
- No lorem ipsum, no "Learn more", no URLs (the platform shows the domain already).

## Layouts

### Centered (default)

```
┌──────────────────────────────────────────────┐
│                  [logo]                       │
│                                               │
│        Your page's promise, in two            │
│              lines at most                    │
│                                               │
│     One supporting line or a proof point      │
└──────────────────────────────────────────────┘
```

For homepages, blog posts, docs, and anything without a strong product visual. Works with every brand.

### Split

```
┌──────────────────────────┬───────────────────┐
│ [logo]                   │ ┌───────────────┐ │
│                          │ │  product      │ │
│ Headline over two        │ │  screenshot,  │ │
│ lines                    │ │  bleeds off   │ │
│                          │ │  the right    │ │
│ Supporting line          │ └───────────────┘ │
└──────────────────────────┴───────────────────┘
```

For product, feature and tool pages that have a screenshot worth showing. The visual bleeds off the right edge (mark it `data-bleed`). Crop the screenshot to its most recognizable corner (usually top-left of the app), not the whole window shrunk down.

### Peek

```
┌──────────────────────────────────────────────┐
│                  [logo]                       │
│        Headline over one or two lines         │
│   ┌──────────────────────────────────────┐    │
│   │  product screenshot rising from the  │    │
└───┴──────────────────────────────────────┴────┘
```

For launches and landing pages where the product UI is the hero. The screenshot is cut off by the bottom edge on purpose (`data-bleed`).

Pick one. If the user hasn't chosen and the page has a good product screenshot, render centered and split and let them pick.

## Per-page images

One image per important page (home, pricing, each feature, each tool, blog posts). Keep the layout, colors and logo position identical across a site so a set of cards reads as one brand; only the headline and visual change.

## Quality checks

1. **Squint test**: at 400px wide (roughly a feed thumbnail) the headline is still readable and is the first thing the eye lands on.
2. **Crop test**: nothing important within 64px of an edge; no half-cut letters or logo.
3. **Two-line rule**: the headline is one or two lines.
4. **Font**: the render uses the real brand font, not a fallback (the render script warns).
5. **Contrast**: headline ≥ 7:1 against the field.
6. **Size**: 2400 × 1260 (or 1200 × 630 at `--scale 1`), under ~1 MB.

## Meta tags

```html
<meta property="og:image" content="https://example.com/og-pricing.jpg">
<meta property="og:image:width" content="2400">
<meta property="og:image:height" content="1260">
<meta property="og:image:alt" content="Simple pricing for teams of every size">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://example.com/og-pricing.jpg">
```

The URL must be absolute (with `https://` and the domain). Framework equivalents:

- **Next.js (app router)**: `export const metadata = { openGraph: { images: [{ url: '/og-pricing.jpg', width: 2400, height: 1260 }] }, twitter: { card: 'summary_large_image' } }` with `metadataBase` set in the root layout.
- **Nuxt**: `useSeoMeta({ ogImage: 'https://example.com/og-pricing.jpg', twitterCard: 'summary_large_image' })`.
- **Astro / SvelteKit / plain HTML**: the `<meta>` tags above in the page `<head>`.

After deploying, check with a card validator (opengraph.xyz, or LinkedIn's Post Inspector). Platforms cache images; change the file name (`og-pricing-v2.jpg`) to force a refresh.
