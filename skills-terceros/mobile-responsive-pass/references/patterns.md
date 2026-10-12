# Mobile patterns: plain CSS and Tailwind

Every pattern is shown twice: **plain HTML/CSS** (works in any framework, including CSS modules and scoped styles) and **Tailwind**. In JSX, `class` becomes `className`; nothing else changes.

The breakpoint is 640px throughout (`sm:` in Tailwind, `@media (max-width: 639px)` in CSS). Swap in the project's own breakpoint if it has one.

In plain CSS, keep the desktop rule untouched and add the mobile override in a media query **after** it. Don't rewrite the desktop rule as mobile-first; that touches desktop.

---

## 1. The mobile-down scale

**Plain CSS**

```css
/* existing desktop rules stay as they are */
.section        { padding: 96px 32px; }
.section h2     { font-size: 40px; line-height: 1.15; margin-bottom: 48px; }
.card           { padding: 32px; }
.features       { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; }

/* mobile overrides */
@media (max-width: 639px) {
  .section      { padding: 48px 20px; }
  .section h2   { font-size: 26px; line-height: 1.2; margin-bottom: 32px; }
  .card         { padding: 20px; }
  .features     { grid-template-columns: 1fr; gap: 32px; }
}
```

**Tailwind**

```html
<!-- before -->
<section class="py-24 px-8">
  <h2 class="text-4xl mb-12">…</h2>
  <div class="grid grid-cols-3 gap-10">
    <div class="p-8">…</div>
  </div>
</section>

<!-- after: unprefixed = mobile, sm: = the original desktop value -->
<section class="py-12 px-5 sm:py-24 sm:px-8">
  <h2 class="text-[26px] leading-tight mb-8 sm:text-4xl sm:mb-12">…</h2>
  <div class="grid grid-cols-1 gap-8 sm:grid-cols-3 sm:gap-10">
    <div class="p-5 sm:p-8">…</div>
  </div>
</section>
```

Common Tailwind swaps:

```
py-16 / py-20 / py-24     →  py-12 sm:py-16 / sm:py-20 / sm:py-24
text-3xl / text-4xl (h2)  →  text-[26px] sm:text-3xl / sm:text-4xl
text-lg (body)            →  text-base sm:text-lg
text-xs (eyebrow)         →  text-[11px] sm:text-xs
p-8                       →  p-5 sm:p-8
gap-14 / gap-10 / gap-6   →  gap-8 sm:gap-14 / gap-8 sm:gap-10 / gap-4 sm:gap-6
mb-12                     →  mb-8 sm:mb-12
w-12 h-12 (icon tile)     →  w-10 h-10 sm:w-12 sm:h-12
```

---

## 2. Don't double-pad: hide the background, flatten the card

**Plain CSS**

```html
<section class="cta">
  <div class="cta__bg" aria-hidden="true"></div>   <!-- gradient / image wall -->
  <div class="cta__card">
    <h2>Start your free trial</h2>
    <p>…</p>
    <a class="btn" href="/signup">Get started</a>
  </div>
</section>
```

```css
.cta       { position: relative; padding: 96px 24px; }
.cta__bg   { position: absolute; inset: 0; background: url(wall.jpg) center/cover; }
.cta__card { position: relative; max-width: 560px; margin: 0 auto; padding: 44px 40px;
             background: #fff; border: 1px solid #e5e5e5; border-radius: 20px;
             box-shadow: 0 20px 50px rgb(0 0 0 / .12); backdrop-filter: blur(8px); }

@media (max-width: 639px) {
  .cta       { padding: 48px 20px; }
  .cta__bg   { display: none; }
  .cta__card { padding: 0; background: transparent; border: 0; border-radius: 0;
               box-shadow: none; backdrop-filter: none; }
}
```

**Tailwind**

```html
<section class="relative py-12 px-5 sm:py-24 sm:px-6">
  <div class="hidden sm:block absolute inset-0 bg-[url(/wall.jpg)] bg-cover" aria-hidden="true"></div>
  <div class="relative max-w-xl mx-auto
              p-0 bg-transparent border-0 shadow-none
              sm:px-10 sm:py-11 sm:bg-white sm:border sm:border-neutral-200 sm:rounded-2xl sm:shadow-xl sm:backdrop-blur">
    …
  </div>
</section>
```

---

## 3. One heading that wraps badly

Only the instance changes; the shared token or global `h1` rule stays.

**Plain CSS**

```css
@media (max-width: 639px) {
  .hero__title { font-size: 24px; line-height: 1.15; }
}
```

**Tailwind** (override a `text-display` or `clamp()` utility on this element only)

```html
<h1 class="text-[24px] leading-[1.15] sm:text-display sm:leading-[1.1]">
  Ship landing pages your customers actually read
</h1>
```

---

## 4. 3-column comparison table → stacked cards

**Plain CSS**

```html
<table class="compare compare--desktop">…</table>

<div class="compare compare--mobile">
  <div class="compare__row">
    <div class="compare__label">Setup time</div>
    <div class="compare__pair">
      <div class="compare__us">5 minutes</div>
      <div class="compare__them">2 weeks</div>
    </div>
  </div>
  <!-- one block per table row -->
</div>
```

```css
.compare--mobile { display: none; }

@media (max-width: 639px) {
  .compare--desktop { display: none; }
  .compare--mobile  { display: block; border: 1px solid #e5e5e5; border-radius: 16px; }
  .compare__row     { padding: 16px; border-top: 1px solid #f0f0f0; }
  .compare__row:first-child { border-top: 0; }
  .compare__label   { font-size: 11px; font-weight: 600; text-transform: uppercase;
                      letter-spacing: .06em; color: #737373; margin-bottom: 12px; }
  .compare__pair    { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .compare__us, .compare__them { padding: 12px; border-radius: 8px; font-size: 14px; }
  .compare__us      { background: #ecfdf5; }   /* use the brand's highlight tint */
  .compare__them    { background: #f5f5f5; }
}
```

**Tailwind**

```html
<div class="hidden sm:block overflow-hidden rounded-2xl border">
  <table>…</table>
</div>

<div class="sm:hidden rounded-2xl border divide-y">
  <div class="p-4">                       <!-- repeat per row -->
    <div class="text-[11px] font-semibold uppercase tracking-wider text-neutral-500 mb-3">Setup time</div>
    <div class="grid grid-cols-2 gap-2 text-sm">
      <div class="rounded-lg p-3 bg-emerald-50">5 minutes</div>
      <div class="rounded-lg p-3 bg-neutral-100">2 weeks</div>
    </div>
  </div>
</div>
```

---

## 5. Wrapped chip row → horizontal scroll

**Plain CSS**

```css
.chips { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; }

@media (max-width: 639px) {
  .chips {
    flex-wrap: nowrap; justify-content: flex-start; overflow-x: auto;
    margin: 0 -20px; padding: 0 20px 4px;      /* bleed to the screen edge = page gutter */
    scrollbar-width: none;
  }
  .chips::-webkit-scrollbar { display: none; }
  .chips > * { flex-shrink: 0; }
}
```

**Tailwind**

```html
<div class="flex gap-2 overflow-x-auto -mx-5 px-5 pb-1 [scrollbar-width:none] [&::-webkit-scrollbar]:hidden
            sm:flex-wrap sm:justify-center sm:overflow-visible sm:mx-0 sm:px-0 sm:pb-0">
  <button class="shrink-0 …">All</button>
  …
</div>
```

---

## 6. Hero preview grid: 2 columns → 3 columns on mobile

Six tiles in 3 rows of 2 is more scroll than 2 rows of 3.

```css
@media (max-width: 639px) {
  .hero-grid { grid-template-columns: repeat(3, 1fr); gap: 8px; }
}
```

```html
<div class="grid grid-cols-3 gap-2 sm:gap-4">…</div>
```

---

## 7. Short label on mobile, long label on desktop

```html
<a href="#compare">
  <span class="label-short">Compare plans ↓</span>
  <span class="label-long">See how every plan compares, side by side ↓</span>
</a>
```

```css
.label-short { display: none; }
@media (max-width: 639px) {
  .label-short { display: inline; }
  .label-long  { display: none; }
}
```

```html
<!-- Tailwind -->
<span class="sm:hidden">Compare plans ↓</span>
<span class="hidden sm:inline">See how every plan compares, side by side ↓</span>
```

---

## 8. Peer-card row → swipe carousel

**Plain CSS**

```html
<div class="tiers" data-carousel>
  <article class="tier">…</article>
  <article class="tier tier--featured"><span class="tier__badge">Most popular</span>…</article>
  <article class="tier">…</article>
</div>
<div class="carousel-dots" data-dots-for="tiers" aria-hidden="true"></div>
```

```css
.tiers { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.carousel-dots { display: none; }

@media (max-width: 639px) {
  .tiers {
    display: flex; gap: 12px;
    overflow-x: auto; scroll-snap-type: x mandatory;
    margin: 0 -20px; padding: 16px 20px;        /* edge bleed + room for badges/shadows */
    scrollbar-width: none;
  }
  .tiers::-webkit-scrollbar { display: none; }
  .tier { flex: 0 0 82%; scroll-snap-align: start; }

  .carousel-dots { display: flex; justify-content: center; gap: 6px; margin-top: 8px; }
  .carousel-dots span { width: 6px; height: 6px; border-radius: 999px; background: #d4d4d4; }
  .carousel-dots span.is-active { background: #171717; }
}
```

Dots need a few lines of JS. Plain script, no dependencies:

```html
<script>
  document.querySelectorAll('[data-carousel]').forEach((track) => {
    const dots = track.nextElementSibling;
    if (!dots || !dots.matches('.carousel-dots')) return;
    const cards = [...track.children];
    dots.innerHTML = cards.map(() => '<span></span>').join('');
    const update = () => {
      const i = Math.round(track.scrollLeft / (cards[0].offsetWidth + 12));
      [...dots.children].forEach((d, n) => d.classList.toggle('is-active', n === i));
    };
    track.addEventListener('scroll', update, { passive: true });
    update();
  });
</script>
```

In React/Vue/Svelte, do the same in the component: an `onScroll` handler on the track that stores the active index, and render the dots from the card count.

**Tailwind**

```html
<!-- was: <div class="grid grid-cols-1 md:grid-cols-3 gap-6"> -->
<div class="flex gap-3 overflow-x-auto snap-x snap-mandatory -mx-5 px-5 py-4
            [scrollbar-width:none] [&::-webkit-scrollbar]:hidden
            sm:grid sm:grid-cols-3 sm:gap-6 sm:mx-0 sm:px-0 sm:py-0 sm:overflow-visible sm:snap-none">
  <article class="snap-start shrink-0 w-[82%] sm:w-auto">…</article>
  <article class="snap-start shrink-0 w-[82%] sm:w-auto">…</article>
  <article class="snap-start shrink-0 w-[82%] sm:w-auto">…</article>
</div>
```

If the desktop layout is a custom CSS grid (bento, mosaic, spans), convert it inside the mobile media query instead of wrapping it, and clear the spans:

```css
@media (max-width: 639px) {
  .bento       { display: flex; grid-template-columns: none; overflow-x: auto; scroll-snap-type: x mandatory;
                 gap: 10px; margin: 0 -20px; padding: 0 20px 4px; scrollbar-width: none; }
  .bento__item { flex: 0 0 84%; scroll-snap-align: start; grid-column: auto; grid-row: auto; }
}
```

---

## 9. CTAs: full width, stretched, 44px tall

**Plain CSS**

```css
@media (max-width: 639px) {
  .hero__actions { flex-direction: column; align-items: stretch; gap: 12px; }
  .hero__actions .btn { width: 100%; min-height: 44px; justify-content: center; }
  .text-link-cta { display: inline-block; padding: 12px 0; }   /* 44px tap height */
}
```

**Tailwind**

```html
<div class="flex flex-col items-stretch gap-3 sm:flex-row sm:items-center">
  <a class="btn w-full min-h-11 sm:w-auto" href="/signup">Start free</a>
  <a class="btn-secondary w-full min-h-11 sm:w-auto" href="/demo">Watch the demo</a>
</div>
```

---

## 10. Check for horizontal overflow

Run in the browser console (or a headless script) at a 390px viewport:

```js
document.documentElement.scrollWidth <= window.innerWidth
// find the culprits:
[...document.querySelectorAll('body *')].filter(el => el.getBoundingClientRect().right > window.innerWidth + 1)
```

Common causes: fixed `width` in px on images or cards, long unbroken URLs or emails (`overflow-wrap: anywhere`), `100vw` widths (use `100%`), and negative margins without a matching `overflow-x: clip` on the section.
