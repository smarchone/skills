---
description: 'Build or revise a one-screen project landing page (GitHub Pages docs/index.html) that sells the idea while asking for as little attention as possible. Use when the user wants a GitHub page, landing page, project homepage or "docs page that sells it", or is iterating on its slogan, layout, spacing or mobile view.'
metadata:
  tags: "landing page, GitHub Pages, copywriting, design taste"
  source: "Distilled from the cf-tunnel docs/ iterations (Nov 2026). Exemplar: references/exemplar.html"
---

# github-page

One static HTML file that sells a project in ~20 seconds. **Attention is scarce**: every element must earn its place, and the reader should never have to work to read it.

The reference is `references/exemplar.html` (cf-tunnel). Read it before building; if it isn't next to this file, fetch https://raw.githubusercontent.com/smarchone/skills/main/taste/github-page/references/exemplar.html. Reuse its structure and tokens; swap the content.

## The non-negotiables

1. **The whole page fits on one laptop screen.** The footer must be visible without scrolling at 1366×768 and 1280×800. This is a must, not a nice-to-have. Every addition gets measured against it; if something pushes the footer, cut or fold something else.
2. **Narrow column: ~640px.** Wide lines cost eye travel, and readers choose not to read. Never go wider to "make room"; shorten copy instead.
3. **One box.** The get-started terminal is the only framed element, because that's where people act. Everything else sits on the background as text. Too many boxes = noise. (Small rounded pills in the flow line are fine.)
4. **Calm but not bland.** Removing everything made it bland and stopped selling. Keep: a strong hero, one accent gradient phrase, a problem list, three benefit columns, a request-flow line. Remove: extra panels, second accent colours, decorative signals.
5. **Copy fits its lines.** No widows (a lone word on the last line). If a line wraps badly at the target width, rewrite the copy; don't shrink the layout.

## Page anatomy (top to bottom)

| # | Block | Rule |
|---|---|---|
| 1 | `~/ owner/repo` mono path | Small, dim, links to the repo. Left-aligned above the hero. |
| 2 | Hero + GitHub icon | Big hook line (~40px) + smaller subheading (~20px) with the payoff in accent gradient. GitHub icon (~38px, dim → white on hover) right-aligned to the content edge, same row. |
| 3 | tl;dr | One paragraph, inline `TL;DR` label. Concrete: what you send, what they see, what happens when you stop. |
| 4 | The problem | Label + 3 `×` bullets. Each a pain the reader already feels. |
| 5 | Pitch | 3 columns: mono label / short white claim / one dim line (≤2 lines). Caveats live here (amber inline text), not in a separate box. |
| 6 | Flow | How it works as pills: `user → link → … → localhost`. The key hop in accent, the endpoint in white. |
| 7 | Get started | Eyebrow: `Get started · ~1 min · needs X, Y` + `copy` button. Terminal with `$` prompts and dim `#` comments. Copy button copies commands only (strips prompts and comments). |
| 8 | Footer | `made with ♥ · [gh icon] @owner/repo`. Red heart (`#ff5c7a`). Nothing else ("more from…" links got cut). |

## Copywriting

- **Lead with the hook, then explain.** "One permanent link." large; the behaviour beneath it smaller.
- **Name both states** when the product has them (on/off, up/down). The distinctive half is the memorable half.
- **Keep the user's verbs.** If they write "exposes … shows …", don't "tighten" them away. Offer edits as numbered variants with a pick; don't silently rewrite their wording.
- **Benefits as reasons to care**, each tied to a pain from the problem list.
- **Honest caveats inline** ("Basic auth. For demos, not anything sensitive.") in warn colour.
- **Don't repeat** the hero in the benefit columns.
- Iterating on a slogan: give a table of 5–10 variants grouped by angle, say which you'd pick and why, keep line lengths that fit the hero at desktop *and* 390px.

## Visual system

Dark, mono-accented, one accent hue. Copy the `:root` block from the exemplar. Key tokens:

- `--bg #0c0d10`, `--fg #c4c7cf`, `--dim #7d828e`, `--faint #565b66`, `--white #e8e9ed`, `--accent #aab4ff` (+ soft fill / line variants), `--warn #e0a85a`.
- Sans (system / Inter) for prose, mono for labels, paths, code, eyebrows. Labels: 11–12px mono, uppercase, letter-spacing .1em, accent or faint.
- Hero gradient on one `<em>` only. Faint radial accent glow at the top of the body.
- **Vertical rhythm scales with viewport height**: `--gap: clamp(16px, calc((100svh - <content-height>px) / <n-gaps>), 56px)`. Roomy on tall screens, tight on short ones, footer always in view. Recompute `<content-height>` when content changes.
- Match the owner's other pages (fonts, colours, GA property) when they point to one.

## Mobile (≤600px)

- Pitch columns stack. Hide terminal comments (commands must fit width; split long commands like `git clone … && cd` into two lines).
- Drop secondary eyebrow bits (`~1 min`, prerequisites).
- Flow becomes a **vertical rail**: one hop per row, dots on a thin line, accent dot with glow on the key hop, white dot on the endpoint, arrows hidden. Never let pills wrap with stranded arrows.
- 16px side gutter, no horizontal scroll.

## Extras

- Google Analytics tag (reuse the owner's property if they have one) plus a `copy_get_started` event on the copy button: it marks who went past reading.
- No build step, no external JS. One file in `docs/`.

## Workflow

1. Read the exemplar and the project README. Ask for the pitch in one line if it isn't given.
2. Build `docs/index.html` from the anatomy above.
3. **Verify with screenshots and measurements**, not by eye from code: desktop 1280×800, 1366×768, 1440×900, and phone 390px. Measure footer bottom vs `innerHeight` (e.g. with `chrome-devtools-axi`) and report it as a small table.
4. When trying a big direction change, write it as `docs/v2.html` beside the current page so the user can compare; delete the losers once they pick.
5. Report each change in terms of what the reader sees, and say plainly what you did *not* check (e.g. phone width this round).
6. Don't commit until asked.

## Anti-patterns (each one was tried and rejected)

- Cards with borders/backgrounds for every section ("too many boxes").
- A separate caution/heads-up box (pushes the footer; fold it into a pitch column).
- Install steps in a sticky side column or right margin (shifts or splits attention).
- Wide content (800px+) to fit more.
- Per-sentence line breaks in the tl;dr (adds height, reverted).
- Over-minimal "plain text only" variant (too bland, doesn't sell).
- Extra panels below get-started ("Expose a service", "What visitors see").
