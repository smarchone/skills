---
name: explain-stories
disable-model-invocation: true
description: Explains a concept, idea, technical topic, blog post, article, or file by telling it through stories rather than abstractions. Auto-detects whether the target already contains real stories, anecdotes, or worked examples — if so, extracts and reformats each into a consistent Setup → Conflict → Resolution → Lesson structure. If the target is purely conceptual with no stories in it, invents one clarifying illustrative story in the same structure. Use whenever the user asks to "explain this as a story", says "explain:stories", wants a concept explained "like I'm five" via narrative, asks "what stories are in this post/article", wants an anecdote-driven breakdown of something dry or technical, or asks for a narrative explanation of a concept, paper, business idea, codebase, or file. This differs from a structural/craft breakdown of writing (thesis, argument shape, rhetorical devices) — reach for THIS skill when the user wants the idea explained through story, not an analysis of how the writing itself is built.
---

# Explain: Stories

People remember and understand causal, character-driven narratives far better than they remember
abstract propositions. A bullet point says "distributed caches invalidate stale data via TTLs." A
story says "the team kept serving yesterday's prices until a customer complained, so they gave every
cached price a expiration clock." The second one sticks. The job of this skill is to find or build
that second version.

## Two modes, auto-detected

Before writing anything, read the whole target (fetch the full URL or file — don't work from a
snippet or summary) and decide which situation you're in:

1. **Stories already exist in the target.** Blog posts, case studies, papers with worked examples,
   product retrospectives, and personal essays often already carry real anecdotes: a named person or
   team, something that happened, a complication, and an outcome. If you find one or more of these,
   your job is *extraction and translation*, not invention. Pull out what's really there and pour it
   into the structure below — don't embellish or add details that aren't in the source.

2. **No story exists — it's a bare concept.** A lot of technical or business writing states
   mechanisms and claims with no narrative at all ("eventual consistency means replicas converge
   over time"). Here your job is *invention*: build exactly one small, concrete story whose events
   map cleanly onto the mechanics of the concept, so a reader who doesn't know the jargon can still
   feel why it's true. Pick a scenario that mirrors the actual causal structure of the idea — the
   story should be a working model of the concept, not a decorative fable bolted on top of it.

Most targets are one or the other, but a target can be mixed: a post might tell one real story
about its main point while leaving a supporting sub-concept unillustrated. In that case, extract the
real one and invent only what's missing — and label each block so the reader always knows which is
which (see below).

## The structure — use it for every story, extracted or invented

Consistency is the point: once the reader knows the shape, they can scan many stories quickly
instead of re-parsing prose each time. Use this exact template for each story:

```
### [Story title — short and evocative]
*(from the source / illustrative analogy)*

**Setup:** Who/what, and the situation before anything went wrong or was at stake.
**Conflict:** What went wrong, what was uncertain, or what tension had to be resolved.
**Resolution:** What actually happened or was decided, and how the tension resolved.
**Lesson:** The one idea this story is standing in for — tie it explicitly back to the concept.
```

Keep each field to a sentence or two — the discipline of compressing to one line per beat is what
keeps this skill from turning into a retelling of the whole source. If the source doesn't state a
lesson outright, infer the most reasonable one from context, but don't present an inference as a
direct quote.

Always mark whether a story is `(from the source)` or `(illustrative analogy)` — a reader relying on
this for research needs to know which parts are the author's actual account and which parts you
made up to help the explanation land.

## Multiple stories

If the target contains several real stories, give each one its own block in the order they appear
(or grouped logically if they're scattered through the piece) — don't cherry-pick down to "the best
one," since the user may be relying on this to see everything the source actually said. After all
the blocks, add a short closing paragraph connecting them back to the target's central idea. Skip
the closing paragraph if there's only a single story that already speaks for itself.

## Edge cases worth handling deliberately

- **Can't access the target** (broken URL, missing file, empty paste): say so plainly and stop —
  don't invent a story to cover for missing input.
- **Target is already just a story** (e.g., someone pastes a personal anecdote and asks you to
  "explain" it): reformat it into the structure rather than declining — restructuring for clarity is
  still the job.
- **Concept is genuinely simple**, and forcing a four-part story would be padding: it's fine for
  Setup or Conflict to be a single short clause. Don't manufacture drama that isn't there.
- **Multiple unrelated concepts in one target**: it's usually clearer to give each concept its own
  story rather than forcing one mega-story to cover everything — check with the user if it's unclear
  whether they want one unifying narrative or several small ones.
