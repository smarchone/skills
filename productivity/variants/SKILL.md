---
name: variants
description: Plan a build by turning research (a doc or the current conversation) into a brief, then the brief into 3-5 concrete build variants, simplest first, each shown through examples. `/variants brief [research.md]` distills a research or brainstorm doc (e.g. RESEARCH.md from an intuition panel), or the research and conversation in the current session, into BRIEF.md (pain, ideas, prior art, components, directions, constraints, axes), and flags when nobody checked whether the wheel is being reinvented. `/variants [BRIEF.md]` writes variants/N-<name>.md (file layout, storage example, contract, pipeline, compounding loop, sample run, trade-offs) plus a comparison README. Use when the user runs /variants, or asks for "variations of how to build this", design options, alternative architectures, or a brief/prompt doc from research.
---

# Variants

The point is to get a **feel** for a design before committing to one. Variants are shown through concrete examples (real files, real data, a real run), never as abstract pros and cons.

```
research (RESEARCH.md or this session) ──/variants brief──▶ BRIEF.md ──/variants──▶ variants/*.md
```

## Subcommands

| command | reads | writes |
|---|---|---|
| `/variants brief [path]` | research doc (`path`, else `RESEARCH.md`, else the current session) | `BRIEF.md` |
| `/variants [path]` | brief (default `BRIEF.md`; falls back to `TODO`) | `variants/README.md` + `variants/N-<slug>.md` |
| `/variants more <idea>` | brief + existing variants | one more `variants/N-<slug>.md`, README row |

Bare `/variants` with no brief but research (a doc or this session): run `brief` first, show it, then continue.

If `.signals/` exists, read `.signals/vocab.md` and use its terms everywhere.

---

## `brief`: research → BRIEF.md

The brief is the prompt for the variants. It holds **what was decided**, not the whole conversation.

1. Find the source. Use `path` if given, else `RESEARCH.md` if it exists, else the research and conversation in the current session. If both a doc and relevant session discussion exist, use both; the later one wins on conflicts. Write the source line accordingly (`RESEARCH.md`, `session`, or `RESEARCH.md + session`).
2. Read the whole source. Fill **every** section from it; don't invent content the source doesn't hold. Extract into the sections in [brief-template.md](brief-template.md). Rules:
   - **The user's words win.** When a persona suggested X and the user said Y, keep Y. Drop suggestions the user never took up, or list them under directions as "open".
   - Things the user deferred ("later; not now") go under `directions → later`, never into ideas.
   - Hard limits (cost, legal, rate limits, "run on command") go under `constraints`. Every variant must honor them.
   - Use bullets, short lines, the user's terminology, and no prose.
3. **Validate prior art (am I reinventing the wheel?).** Fill `prior art` only from what the source actually found: existing products, repos, skills or tools, each with why it isn't enough. Don't search for it yourself. If the source never checked, write `prior art: ⚠ not checked` and keep going.
4. Write the **axes** section: the 3-6 dimensions where reasonable designs would differ (e.g. storage shape, where memory lives, unit of fetching, code vs agent, how the loop compounds). These are what the variants will vary on. This is the most important section, so derive it from tensions in the research, not from a generic list.
5. Write `BRIEF.md` (or update the existing file if the user points to one, e.g. `TODO`, keeping its headings). Tell the user the axes in 2-3 lines and ask whether any are missing.
6. If prior art is `⚠ not checked` (or only lists things without saying why they fall short), end the reply with a reminder:
   > ⚠ Reinventing the wheel? Nobody checked for existing tools, repos or products that already do this. Look before `/variants`, then re-run `/variants brief`.

   `/variants` on a brief with `⚠ not checked` repeats this reminder once before writing variants.

## `/variants`: BRIEF.md → variants/

1. Read the brief. Read the vocab if it exists.
2. Choose **3-5 variants**, ordered simplest → most capable. Each one should be a coherent position on the axes, not a random mix. Good sets usually include:
   - the **weekend version** (fewest files, no state),
   - one or two that **add one capability each** (memory, replay, auto-growth),
   - one **orthogonal** take (e.g. agent/prompt-driven instead of code, or buy instead of build).
   Drop any variant that breaks a constraint.
3. Write each `variants/N-<slug>.md` following [variant-template.md](variant-template.md). Rules:
   - Examples use **the project's real domain data** (real names, real URLs shapes, real fields from the brief), never `foo/bar`.
   - Code stays short: one interface, about 20 lines at most. Show the shape, don't build it.
   - Every variant uses the same vocabulary and the same example entity, so they can be compared line by line.
   - Make "Pick it when" one honest sentence.
4. Write `variants/README.md`:
   - one comparison table: a column per axis plus `effort`, a row per variant, with links,
   - a small ASCII diagram of how the variants relate (which one grows into which, which ones combine),
   - **a likely path**: your recommendation in 2-3 lines, including hybrids.
5. Reply in the terminal with the table and the recommendation only. The files hold the detail.

## `more`

`more <idea>`: write one extra variant from the user's idea using the same template, and add it to the README table and diagram.

## Don'ts

- Don't survey every possible design. 3-5 variants, each with a reason to exist.
- Don't write "it depends". Each variant takes a position; the README recommends one.
- Don't put deferred features into the simple variants.
