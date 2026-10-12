# Typography

## Type scale
- **Define a fixed type scale.** Never pick font sizes ad hoc.
- **Linear scales don't work.** Need small jumps at the low end, larger jumps at the top.
- **Modular scales (ratio-based) have two problems:** fractional pixel values (subpixel rounding issues) and not enough sizes for UI work. Round them, or hand-craft instead.
- **Hand-crafted scales are best for UI.** Total control, no rounding errors.
- **Avoid `em` units in type scales.** Compounding nesting makes the rendered size fall outside your scale. Use `px` or `rem`.

## Font choice
- **Safe default for UI:** neutral sans-serif (Helvetica-like) or the system font stack.
- **Skip fonts with fewer than ~5 weights.** Generally a sign of less attention to detail. Filter font directories accordingly.
- **Don't use condensed/short-x-height fonts for UI text.** They're built for headlines.
- **Popular fonts are probably good fonts.** Sort by popularity to shortlist.
- **Steal from sites you admire** — inspect their type choices.

## Line length
- **45–75 characters per line** for paragraph text. (~20–35em width.)
- **Limit paragraph width even when the container is wider** to accommodate images/other elements. Mixed widths look more polished, not less.

## Vertical alignment of mixed sizes
- **Align mixed font sizes by baseline, not center.** Eyes naturally read from the baseline. Centering offsets the baseline and looks off.

## Line-height
- **Line-height and line length are proportional.** Narrow text → ~1.5 line-height is fine. Wide text → up to ~2.
- **Line-height and font size are inversely proportional.** Small text → taller line-height. Large headlines → line-height as low as 1.

## Links
- **Not every link needs a color.** In link-dense UIs, a colored underlined "pop" treatment is overbearing.
- Use heavier weight or darker color for subtle emphasis. Ancillary links can show underline/color only on hover.

## Alignment
- **Default: left-align** (for LTR languages). Match the reading direction.
- **Don't center long-form text.** Centering works for headlines or short blocks (2–3 lines max). If a centered block is too long, shorten the copy.
- **Right-align numbers in tables** so decimals line up.
- **Hyphenate justified text** to avoid awkward word-gaps. Justified text suits print-mimicking layouts only.

## Letter-spacing
- **Default: trust the type designer.** Don't tweak.
- **Tighten letter-spacing on headlines** when using a UI-text font for large display (e.g., Open Sans at headline sizes). Don't do the reverse — headline fonts don't work small.
- **Increase letter-spacing on all-caps text** for legibility. Caps lack the visual variety (ascenders/descenders/x-height) that the default spacing assumes.
