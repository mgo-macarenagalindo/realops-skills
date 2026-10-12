# Spacing & Layout

## Whitespace
- **Start with too much whitespace, then remove.** Don't add until "not actively bad" — add until great, then trim.
- **Dense UIs (dashboards) are a deliberate exception**, not a default.

## Sizing system
- **Define a spacing/sizing scale in advance.** No arbitrary pixel-tuning.
- **A linear scale (e.g., multiples of 4) doesn't work** — relative differences matter more than absolute.
- **Each step in the scale should differ from the next by ~25% or more.** Below that, the values are indistinguishable.
- **Start from a sensible base** (16px is great — divides cleanly, matches default browser font-size).
- **Tighter at the small end, wider gaps at the large end** (mimicking how human perception scales).

## Layout width
- **Don't fill the screen just because you can.** If 600px is enough, use 600px.
- **Don't make a section full-width to match another section.** Each piece gets the width it needs.
- **Shrink the canvas if you're struggling.** Design mobile-first at ~400px when the small layout is what matters.
- **Use columns instead of width** when a narrow component looks unbalanced — split content (e.g., supporting text in a second column) rather than stretching.

## Grids
- **Grids are overrated.** Don't outsource all layout decisions to a 12-column system.
- **Not all elements should be fluid.** Sidebars especially: give them a fixed width optimized for their contents; let the main area flex.
- **Don't shrink an element until you have to.** Use `max-width` so things only collapse when the viewport actually requires it — not because the grid says so.

## Relative sizing
- **Relative sizing doesn't scale across breakpoints.** A 2.5em headline on desktop is wrong on mobile.
- **Rule:** large elements shrink *faster* than small ones at small screens. The gap between large and small narrows on mobile.
- **Don't tie padding to font-size** in components. Buttons feel right when padding scales *disproportionately* — generous at large sizes, tighter at small sizes.

## Ambiguous spacing
- **Whenever spacing groups elements, the space *around* the group must exceed the space *within* it.**
- Common failures:
  - Form: label-input gap = field-to-field gap → fields blur together. Fix: increase between-field gap.
  - Article: heading not visually attached to its section because top margin = bottom margin.
  - Lists: bullet spacing = single-bullet line-height.
  - Horizontal layouts: same problem, sideways.
