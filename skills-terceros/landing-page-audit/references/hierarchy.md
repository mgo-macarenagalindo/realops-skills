# Hierarchy

## Principles
- **Not all elements are equal.** Deliberately de-emphasize secondary/tertiary content. Noise = bad design.
- **Size isn't everything.** Use weight and color to create hierarchy, not just size — primary content shouldn't have to be huge, and secondary shouldn't have to be tiny.

## Color & weight defaults for text
- Use **2–3 text colors max**: dark (primary), grey (secondary), light grey (tertiary).
- Use **2 font weights max** for UI: normal (400 or 500), bold (600 or 700).
- **Avoid font weights below 400** for UI work — unreadable at small sizes. To de-emphasize, use lighter color or smaller size instead.

## Grey on colored backgrounds
- **Don't use grey text on colored backgrounds.** The effect we like is *reduced contrast*, not "greyness."
- **Don't use white-with-reduced-opacity** on colored backgrounds — looks washed out/disabled, and bleeds when over images/patterns.
- **Instead:** hand-pick a new color matching the background hue, then tweak saturation/lightness until contrast feels right.

## Emphasize by de-emphasizing
- When the focal element won't pop, **don't push it harder — push the competing elements back** (softer color, no background, etc.).

## Labels
- **Labels are a last resort.** Format alone often communicates type (e.g., `$19.99`, `(555) 555-5555`, `jane@x.com`). Context often does too.
- **Combine labels into the value** when possible: "12 left in stock" beats "In stock: 12"; "3 bedrooms" beats "Bedrooms: 3".
- When you must use a label, **treat it as secondary** — smaller, lower contrast, lighter weight.
- **Emphasize the label only** when users scan *for* the label (e.g., tech specs pages where someone hunts "depth", not "7.6mm").

## Semantic markup ≠ visual size
- **Separate visual hierarchy from document hierarchy.** An `h1` doesn't have to look big. Section titles are often labels — style them small.
- Pick HTML elements for semantics; style them however the visual hierarchy demands. Hide section titles visually if the content speaks for itself.

## Weight vs. contrast
- **Icons feel heavy.** When icons sit next to text, lower the icon's contrast (softer color) to balance.
- **Thin borders** (1px) that need to be visible: increase weight (thicker border) rather than darkening to a harsh color.

## Button hierarchy (semantics ≠ visual weight)
Every page has a pyramid:
- **Primary action** → obvious. Solid, high-contrast background.
- **Secondary actions** → clear but not loud. Outline or low-contrast background.
- **Tertiary actions** → discoverable, unobtrusive. Style as links.
- **Destructive ≠ big red.** If destroy isn't the page's primary action, don't style it as primary. Use a confirmation step where the destructive action *is* primary, and apply the loud red there.
