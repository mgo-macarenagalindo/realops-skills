# Depth

## Light source
- **Light always comes from above.** This is the one rule for every shadow/highlight decision.
- **Raised elements:** show a lighter top edge (top facing the sky) and a dark shadow below.
- **Inset elements:** show a darker top edge (top blocked from the sky) and a lighter bottom edge.

## Raised element construction
1. Reveal the **top edge slightly lighter** than the face (top border or inset shadow with small positive vertical offset).
2. **Pick the lighter color by hand** — don't use semi-transparent white (it desaturates).
3. Add a **dark drop shadow below** with slight vertical offset.
4. **Keep blur radius small** (~few px). Real-world shadows from raised objects are sharp.

## Inset element construction
1. Show the **bottom edge slightly lighter** (bottom border or inset shadow with small negative offset).
2. Add a **dark inset shadow at the top** so the lip casts a shadow down into the well.

Use for text inputs, checkboxes, wells.

## Elevation via shadows
- **Bigger blur + larger offset = closer to the viewer.** Closer-feeling elements demand more attention.
- **Buttons:** small shadow.
- **Dropdowns:** medium shadow.
- **Modals:** large shadow.
- **Define an elevation system: ~5 fixed shadows**, smallest to largest, roughly linear progression.
- **Use shadows for interaction feedback:** lift on drag (bigger shadow), depress on click (smaller/no shadow).

## Two-part shadows
Real shadows are two phenomena:
- **Large soft shadow** = light blocked by the object. Bigger blur, larger offset, lighter.
- **Tight dark shadow** = ambient light can't reach the contact zone. Small blur, small offset, darker.
- **At higher elevation, the tight contact shadow fades** (object is further from the surface). Lowest elevation: distinct contact shadow. Highest elevation: almost none.

## Depth without skeuomorphism
- **Lighter = closer, darker = farther** (with shades of the same color). Use color alone for depth in flat designs.
- **Solid shadows** (vertical offset, zero blur) add lift without breaking flat aesthetic.

## Layering via overlap
- **Overlap elements** across boundaries (e.g., card straddling two background sections) to create a sense of layers.
- **Make an element taller than its parent** so it overhangs on top/bottom.
- **Overlapping images:** give each an "invisible border" matching the background color, so they don't clash where they meet.

## Don't overdo it
- Borrowing real-world cues adds depth; trying to be photo-realistic creates noise. Stop early.
