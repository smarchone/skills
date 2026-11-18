---
description: 'Turn rough idea notes into a short, punchy blog post as one HTML page, built around one animated GIF that shows the idea and one small inline diagram. Use when the user has a notes file (bullets, half-sentences, an illustration they describe in words) and wants a blog post, essay or explainer from it, or wants an illustration or GIF for an existing post.'
metadata:
  tags: "blog, essay, illustration, gif, writing voice, design taste"
  source: "Distilled from the '10x / Head of Agents' post (Nov 2026). Exemplar: references/exemplar.html"
---

# visual-blog

A blog post where **the picture carries the argument** and the words explain the picture. The reader should get the idea from the GIF alone, then read to see why.

The reference is `references/exemplar.html` with its GIF `references/10x-side-by-side.gif`. Read the HTML before building; if it isn't next to this file, fetch https://raw.githubusercontent.com/smarchone/skills/main/taste/visual-blog/references/exemplar.html. Reuse its structure and tokens; swap the content.

## Input

- A notes file: rough bullets, half-sentences, typos. Treat every bullet as a claim to land, not text to copy.
- Usually an illustration described in words ("two vertical arrows, one per side, each row is a project"). Build exactly that picture first; it is the post's spine.
- Often a link to an earlier post. Read it for **voice and vocabulary**, then reuse its terms (e.g. "shared abstraction", "altitude") so the posts read as a series. Link it at the end.

## Voice

- Short sentences. Aphoristic. A wry line now and then. "The agent types; you think."
- Open by killing the obvious reading of the title ("10x doesn't mean typing faster"), then give the real one.
- One **pull line** per major section: a two-line thesis in display type with one or two words in the accent colours.
- Concrete examples beat abstractions: a task vs. a goal shown as two side-by-side cards with real-looking content.
- Keep the user's own phrases when they're good ("doing more by doing less"). Use them as pull lines rather than rewording them.
- No em-dash asides, no "not X but Y" scaffolding, no emoji.

## Page anatomy (top to bottom)

| # | Block | Rule |
|---|---|---|
| 1 | Eyebrow + title + dek | Mono eyebrow names the series. Title is two short lines, with the two roles in their two colours. Italic dek with the question the post answers. |
| 2 | Hook | 2–3 short paragraphs, then the pull line with the thesis. |
| 3 | The GIF | Full width of the 860px main, in a bordered card, mono caption that says how to read it (what's left, right, the dashed line). Good alt text describing the motion. |
| 4 | "The picture" | Walk through the GIF in prose: what happens on each side and the one thing that changed. |
| 5 | Concept sections | One `h2` per note cluster. Rules as a label/claim list (mono uppercase label in the role's colour, bold lead phrase, one sentence). |
| 6 | Second diagram | One small inline SVG for the idea that is a 2D trade-off (e.g. "how many" × "how long"): labelled regions, arrows toward the good corner. Theme tokens only. |
| 7 | Close | A last pull line, a hairline rule, a mono aside linking the earlier post. |

The reading column is ~66ch. Only figures go wider.

## The GIF

- **Contrast side by side, on one clock.** The bad way on the left, the good way on the right, the same events arriving at the same moment, so the difference is the only thing that moves. A single-panel version that plays one way after the other is the fallback.
- **Growth goes upward.** Things that accumulate (context, projects, time) stack from a baseline and the axis arrows grow with them.
- **Show the failure.** A budget line, red hatching past it, a meter that goes over 100%, a counter of what's waiting. End on a held frame with a one-line verdict in each panel.
- Light palette with the same tokens as the page, Avenir Next + Menlo, render at 2× and downscale, ~20 fps, ~12 s, loops, under ~400 KB.
- Build it with `references/make_gif_sbs.py` as the starting point: Pillow draws the PNG frames, ffmpeg turns them into a GIF with `palettegen` and `paletteuse=dither=none`. Pillow goes in a scratch venv. Look at the first, middle and last frames before calling it done, and fix any overlaps (labels hidden under shapes are the usual one).
- Keep the script next to the post so the GIF can be re-rendered.

## Visual system

Copy the `:root` block from the exemplar. Cool grey-blue paper, never cream.

- Two role colours carry the meaning everywhere: `--human` cobalt `#2F43C9` and `--agent` teal `#0B8574`, each with a `-soft` fill. `--warn` `#C8412F` only for the failure state. Dark-theme values are in the exemplar.
- Type: Bricolage Grotesque (display, 700–800), Source Serif 4 (body, 19px), JetBrains Mono (eyebrows, captions, labels, diagram text).
- Cards (border + radius) only for the GIF, the comparison cards and nothing else.

## Workflow

1. Read the notes, the earlier post if linked, and the exemplar.
2. Map every note bullet to a section or a pull line. Say which bullet went where in the report.
3. Build the GIF, then the page around it. Work locally in the notes' folder: `<name>.html`, `<name>.gif`, the GIF script.
4. When the notes file changes, re-read it and fold the new bullets in. Don't rewrite sections the user already liked.
5. Don't publish or commit until asked.
