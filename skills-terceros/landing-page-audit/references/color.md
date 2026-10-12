# Color

## Use HSL, not hex/RGB
- **HSL maps to how humans perceive color** (hue, saturation, lightness). Hex/RGB hide visual relationships.
- **Hue** = position on color wheel (0° red, 120° green, 240° blue).
- **Saturation** = vividness. 0% = grey, 100% = vivid. When saturation is 0%, hue is irrelevant.
- **Lightness** = 0% black → 100% white. 50% lightness = the pure color.
- **HSL ≠ HSB.** In HSB, 100% brightness is white only when saturation is 0%. Browsers only speak HSL. Use HSL for web work.

## Palette structure
A real palette is much bigger than "5 colors". You need three categories:

### Greys
- **8–10 shades.** Backgrounds, text, panels, form controls — almost everything is grey.
- **Avoid true black** — looks unnatural. Start from a very dark grey.

### Primary color(s)
- **One, maybe two.** The brand-defining colors (e.g., Facebook's blue).
- **5–10 shades each.** Light shades for tinted backgrounds (alerts); dark shades for text.

### Accent colors
- **Multiple, used sparingly.** Semantic states (red destructive, yellow warning, green positive) and feature highlights.
- **5–10 shades each.** Add more accent colors if categorizing many items (graph lines, calendar events, tags).
- **A complex UI may need ~10 colors × 5–10 shades each.**

## Building a shade scale
- **Never generate shades on the fly with `lighten()`/`darken()`** — leads to 35 near-identical blues.
- **Choose the base color first.** Rule of thumb: pick a shade that works as a button background.
- **Then pick darkest and lightest shades.** Darkest = text use case; lightest = tinted background use case. An alert component covers both — design one to find them.
- **Then fill the gaps.** Naming: 100 (lightest) → 500 (base) → 900 (darkest). Pick 300 and 700 as midpoints between, then 200/400/600/800.
- **Trust your eyes, not math.** Tweak when colors are in actual UI. But don't add new shades freely — discipline matters.

## Lightness kills saturation
- **As lightness approaches 0% or 100%, saturation's effect weakens.** Lighter shades look washed out unless you bump saturation.
- **Increase saturation as lightness moves away from 50%.**

## Perceived brightness (the hue-rotation trick)
- **Different hues have inherent brightness.** Yellow/cyan/magenta are inherently bright; red/green/blue are inherently dark, even at identical HSL lightness.
- **To brighten without losing color intensity, rotate hue toward the nearest bright peak** (60° yellow, 180° cyan, 300° magenta).
- **To darken without going muddy, rotate toward the nearest dark trough** (0° red, 120° green, 240° blue).
- **Don't rotate more than 20–30°** or it reads as a different color.
- **Especially useful for light colors like yellow:** as you darken, rotate toward orange so dark shades feel warm/rich, not brown.

## Greys don't have to be grey
- **Saturate greys** with a color to set temperature: blue tint = cool, yellow/orange tint = warm.
- **Bump saturation on the lightest and darkest grey shades** so they don't look washed-out next to the mid-greys.

## Accessibility
- **WCAG contrast targets:** 4.5:1 for normal text (<~18px), 3:1 for large text.
- **Flip the contrast** when a colored background gets too dark trying to hit 4.5:1 with white text — use dark colored text on a light colored background instead.
- **Colored text on colored backgrounds:** rotate the hue toward a brighter color (cyan/magenta/yellow) to hit contrast targets without going white.
- **Never rely on color alone.** Colorblind users need a second signal: icons (up/down arrows), labels, or contrast differences (light vs. dark lines on a graph, not just hue differences).
