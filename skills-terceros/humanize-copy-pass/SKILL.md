---
name: humanize-copy-pass
description: Strips AI tells from existing landing-page and marketing copy and tightens it into plain, human prose, without changing its meaning, claims, structure or pitch. Removes hedging, corporate/AI vocabulary ("leverage", "seamless", "unlock", "elevate"), and over-punchy machine cadence ("X, not Y" stacks, two-beat fragments, rule-of-three zingers, em-dash habits). Use when the user says "make this less AI", "humanize this copy", "de-AI this page", "this sounds like ChatGPT", "fix the tone", "remove the AI tells", or "copy pass". Works on pasted text, markdown, or copy inside HTML/JSX/Vue/Svelte templates (edits only the visible text). Not a rewrite: it never re-pitches, reorders sections, or invents claims.
---

# Humanize Copy Pass

A tone and de-AI cleanup pass on copy that already exists. You keep the copy's meaning, claims, structure, point of view and pitch. You only remove the fingerprints of AI and corporate writing and tighten what's left so it reads like a person wrote it.

What this skill **doesn't** do: re-pitch the page, change the angle, write new headlines from scratch, reorder sections, add proof, or turn the copy into a different framework. If the user wants that, say this pass is the wrong tool and stop.

## Inputs

Resolve in order, without asking:

1. **Source.** A file path → read it. Text pasted in chat → use it. A URL → fetch the page and work on its visible copy, then print the cleaned version (you can't write back to a live site). Nothing given → ask the user to paste the copy or point at the file.
2. **Output.**
   - Markdown or plain-text file → overwrite the same file in place.
   - A template or component file (HTML, JSX/TSX, Vue, Svelte, Astro, Liquid…) → edit **only the human-visible strings in place**: text nodes, `alt`, `title`, `aria-label`, `placeholder`, button labels, and the page's `<title>` / meta description. Never touch tags, attributes that aren't copy, class names, variables, interpolations (`{name}`, `{{ price }}`), or code.
   - Copy pasted in chat → print the cleaned copy inline.

You don't need the brand, audience or voice guide for this pass. Never ask for them.

## What to strip

Each of these is a fingerprint. Remove them.

**Hedges and qualifiers**
"perhaps", "might want to consider", "could potentially", "in many cases", "generally speaking", "it's worth noting that", "arguably", "relatively", "fairly", "a bit". Replace with the plain claim, or cut the sentence.

**Throat-clearing openers**
"In today's fast-paced world", "When it comes to X", "It's no secret that", "It's important to understand that", "At the end of the day", "Whether you're a X or a Y". Cut. Start with the noun or the verb.

**Corporate and AI vocabulary**
"leverage", "utilize", "robust", "comprehensive", "seamless(ly)", "cutting-edge", "state-of-the-art", "best-in-class", "world-class", "next-level", "game-changer", "revolutionize", "supercharge", "synergy", "empower", "unlock", "unleash", "streamline", "navigate", "delve", "dive into", "tapestry", "landscape", "realm", "ecosystem", "holistic", "transformative", "elevate", "curated", "foster", "facilitate", "myriad", "plethora", "effortless(ly)", "in a few clicks" (when no clicks are counted). Swap in the plain word for what actually happens: "use", not "utilize"; "help", not "facilitate"; "show", not "showcase".

**Vague abstractions**
"better results", "improved efficiency", "enhanced experience", "peace of mind", "solutions", "take it to the next level". Replace with the concrete thing the copy already means. If the source never says what that is, make it plain and leave it. **Don't invent** a number, feature or customer story to fill the gap.

**Stuffed caveats**
Parenthetical hedges and "results may vary" mid-sentence. Cut, or move to the fine print where they belong.

## AI cadence tells: ration, don't ban

The opposite failure: copy that's punchy in a recognizably machine way. These patterns are fine once. The tell is **repetition and density**. Count each pattern across the whole page, keep the single strongest instance, rewrite the rest as plain statements.

- **Two-beat contrast fragments**: "Your launch ends. Your traffic doesn't." / one-line comebacks ("It doesn't.").
- **"X, not Y" stacks**: "minutes, not weeks", "real feedback, not vanity metrics". One per page at most.
- **Rule of three with a cute third item**: "for founders, marketers, and the chronically busy". Also drumbeat anaphora: "every page, every launch, every test".
- **"Here's…" pivots**: "Here's the thing", "Here's what changes". Cut the pivot, start with the content.
- **Em-dash habit and "It's not just X — it's Y"**: one em-dash construction per page, not per paragraph.
- **Cinematic time-jumps and ticking clocks**: "Three launches later, …", "Every day without X, …".
- **Stock closers and intensifiers**: "so you don't have to", "and that's just the beginning", "actually", "truly", "really", "simply".
- **Self-reused phrases**: the same coined phrase paying off twice. Rewrite the second one.
- **Meta-narration**: "Let's take a look at how it works." "Below, you'll find…". Cut.
- **Emoji bullets and sparkle headers** (🚀 ✨ 💡) on a page that otherwise doesn't use emoji. Remove.

## Landing-page specifics

- **Headlines and subheads**: tighten, don't replace. Keep the same promise and the same key words; cut filler and AI vocabulary. A headline that's already plain stays as it is.
- **CTAs**: keep their meaning and length. "Unlock your free trial" → "Start your free trial". Don't change what the button does or promises.
- **Feature cards**: these collect the most AI vocabulary. Make each card say what the feature does in plain words; keep one card per feature and the same order.
- **Testimonials and quotes**: never edit. They are someone else's words.
- **Numbers, prices, legal text, product names**: never change.
- **Length**: the result should be the same length or shorter. Don't pad short copy.

## Plain-prose tightening

After stripping, tighten without changing meaning:

- **Active voice.** "We check every page" beats "every page is checked by our team".
- **Short sentences.** Split anything that reads as two thoughts. Cut adverbs.
- **Cut filler.** "in order to" → "to"; "the fact that" → cut; "a wide range of" → "many" (or the number, if the copy gives one).
- **Keep the author's words when they're already plain.** Don't swap a fine word for another fine word. Minimal diff is the goal.

## The pass

1. **Read everything first.** Note the tells and tally the cadence patterns before editing, so you ration instead of nuking every instance.
2. **Strip** vocabulary, hedges, openers and stuffed caveats.
3. **Ration** the cadence tells: at most one of each pattern on the page.
4. **Tighten.**
5. **Check for drift.** Every claim, number, feature and promise in the output must already be in the input, in the same order. If you changed what something *says* rather than how it sounds, revert that part.

If the copy is already clean, say so and stop. Don't rewrite for the sake of it.

## Output

- Pasted copy → the cleaned copy only, ready to paste, no preamble.
- File → the file edited in place.

Then, in your reply, a short `## What changed` list: 3–6 bullets naming the biggest moves ("Cut 5 'X, not Y' stacks to 1", "Replaced leverage/seamless/unlock with plain verbs", "Removed emoji bullets from the features list"). Under 80 words. For files, add 3–5 before → after examples of the edits that mattered most so the user can judge the pass without opening a diff.
