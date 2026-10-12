# Images

## Photo quality
- **Bad photos ruin good designs.** Either hire a pro or use high-quality stock (Unsplash, etc.).
- **Never design with placeholders intending to swap in phone snaps later.** It never works.

## Text over images
Background images have light and dark areas — no single text color stays readable across them. Fix by **reducing dynamic range**:

1. **Overlay** — semi-transparent black (for light text) or white (for dark text) layer over the image.
2. **Lower image contrast** — gives finer control than an overlay; adjust brightness to compensate.
3. **Colorize** the image: lower contrast → desaturate → solid fill with "multiply" blend mode. Bonus: ties the image to brand colors.
4. **Text shadow** — for preserving image dynamics. Use a large blur and no offset (looks like a glow, not a shadow). Often combined with mild contrast reduction.

## Scaling — everything has an intended size
- **Don't scale up small icons.** Icons drawn at 16–24px look chunky/under-detailed at 3x–4x. Workaround: wrap the small icon in a larger shape with a background color.
- **Don't scale down screenshots.** A 16px font shrunk 70% becomes a 4px unreadable smear. Options:
  - Take the screenshot at a smaller breakpoint (e.g., tablet).
  - Use a partial screenshot.
  - Draw a simplified, abstracted version (lines instead of text).
- **Don't scale down icons or logos either.** Favicons especially: a 128px logo shrunk to 16px goes to mush. Redraw a simplified version at the target size — you control the compromises, not the browser.

## User-uploaded content
- **Control shape and size.** Don't render images at intrinsic aspect ratio in a layout — center inside fixed containers with `background-size: cover`, cropping overflow.
- **Prevent background bleed** when an upload's background matches your UI background:
  - Use a **subtle inner box shadow**, not a border (borders clash with image colors).
  - Or a **semi-transparent inner border** if you dislike the inset look.
