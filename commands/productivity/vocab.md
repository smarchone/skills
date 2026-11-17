---
description: >-
  Write or refresh a concise vocabulary.md that turns any detailed source (a codebase, blog post, spec, design doc, research) into a steerable abstraction for humans: its core constructs and how they compose. Use when the user asks for a vocabulary, glossary, domain model, concepts or onboarding doc, or "how the pieces fit".
---

# Domain vocabulary

Write a `vocabulary.md` that puts the reader at the right altitude: one level above the detail, one level below the
pitch. The source can be anything detailed: a codebase, a long blog post, a spec, a design doc, a body of research.
From the vocabulary alone, the reader can steer the thing and take decisions ("should we add X?", "is Y in scope?",
"does this argument hold?") without going back to the source.

Three ideas drive everything below:

1. **Composition, not a glossary.** Words alone don't say why each piece exists. Build the whole up one construct at
   a time and show what each one unlocks, so the complexity feels earned.
2. **Direction, not instruction.** "Use Postgres" goes stale. "Relational integrity across tenants; document store
   ruled out for reporting" lets anyone derive the next steps. Record the *why*.
3. **Attention is the budget.** Every line spends the reader's attention. Keep a line only if it would change how
   they think or decide.

## Process

1. **Scope.** Find the source the user means. For a codebase, respect CLAUDE.md rules about which folders to read.
2. **Read the source itself**, not a summary of it. For code, docs tell you intent; code tells you what is true.
3. **Find:**
   - *why* it exists, for whom, and what it deliberately doesn't do or claim;
   - the 4–7 core *constructs*, in the source's own names (more won't fit in a reader's head: group or drop);
   - their *order of composition*: the atom first, each next one adding something the reader would notice (for a
     product, a capability; for an argument, a step in the case); if it adds nothing, it isn't core;
   - one real *running example* to trace through every step;
   - the *decisions* behind the shape and what was *ruled out* (ask the user when the source can't tell you).
4. **Write** the doc below, next to the source unless the user says otherwise.
5. **Verify every name and example against the source.** If a word means different things in two places, pick the
   most authoritative one (for code, the code) and tell the user.

## The doc

```markdown
# <Subject> — Vocabulary

## Where you are
**Above:** the purpose: <who it's for, what they get>.
**Here:** the constructs it's made of and how they compose. Hold these in your head.
**Below:** the detail: <the code, the full post, the spec>. Go there only when changing one construct.
**Does:** … · **Doesn't:** …

## How it's built up
Running example: <one real scenario>.

### 1. **<Atom>** — <what it's for>
> <the example, as this construct: a real detail from the source>

Gives you: <what it unlocks, in the reader's terms>.

### 2. + **<Next>** — <what it adds>
> <the same example, one step further>

Now you get: <what neither piece had alone>.

… <the last step is the whole thing as its audience sees it>

## The whole picture
<Small ASCII diagram with the example flowing through. The core loop or thesis as a one-line code block.>

## Decisions
<4–7 numbered: a bold claim, then one sentence of why.>

## Ruled out
<Table: Option | Why not. Only what someone would plausibly re-propose.>
```

Tag anything not built or not yet settled as *planned*, in place.

## Taste

- **The first screen stands alone.** Someone who stops after the first steps should have a correct, partial picture.
- **One new idea per step.** Never use a term before its step; never re-explain it after.
- **Same example all the way down.** It grows with each step; never switch scenarios.
- **Unlocks in the reader's terms.** "The learner gets instant feedback", not "`judge()` returns a score".
- **Order by dependency, not by where things sit in the source.**
- **Concrete beats abstract.** If the example says it, drop the sentence.
- **Stay at altitude.** No internals, file lists, constants, recipes or hedges ("mostly", "originally") below; no
  slogans the reader can't act on above.
- **About three minutes to read, 60–110 lines.** Longer means it's becoming a manual, so cut.

## Updating

One living doc: new decisions amend it in place, never a new plan file. Keep the existing words, restructure a flat
glossary into the build-up, and re-check every name against the source, since sources drift.
