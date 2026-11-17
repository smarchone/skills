---
name: vocab
description: >-
  Write or refresh a concise vocabulary.md that turns any detailed source (a codebase, blog post, spec, design doc, research) into a steerable abstraction for humans: its core constructs and how they compose. Use when the user asks for a vocabulary, glossary, domain model, concepts or onboarding doc, or "how the pieces fit".
---

# Domain vocabulary

Write a `vocabulary.md` that puts the reader at the right altitude: one level above the detail, one level below the
pitch. The source can be anything detailed: a codebase, a long blog post, a spec, a design doc, a body of research.
From the vocabulary alone, the reader can steer the thing and take decisions ("should we add X?", "is Y in scope?",
"does this argument hold?") without going back to the source.

Three ideas drive everything below:

1. **Each section is a different view.** What flows, which settings combine, which part does what, which rules
   decide, what was refused. Five views of one system, none repeating another. Then one closing summary puts them
   back together.
2. **Direction, not instruction.** "Use Postgres" goes stale. "Relational integrity across tenants; document store
   ruled out for reporting" lets anyone derive the next steps. Record the *why*.
3. **Attention is the budget.** Every line spends the reader's attention. Keep a line only if it would change how
   they think or decide.

## Process

1. **Scope.** Find the source the user means. For a codebase, respect CLAUDE.md rules about which folders to read.
2. **Read the source itself**, not a summary of it. For code, docs tell you intent; code tells you what is true.
3. **Find the shape before the words:**
   - *why* it exists, for whom, and what it deliberately doesn't do or claim;
   - the *main flow*, in one line;
   - the *independent settings* every use combines (e.g. *what* × *how* × *how much help*), if there are any.
     Often the single most useful insight;
   - the 4–7 *parts*, each with one job (more won't fit in a reader's head: group or drop);
   - the *design rules* behind the shape and what was *ruled out*. Infer them from how the source is built; ask
     the user for the why when the source can't tell you;
   - the pairs a newcomer will *confuse*.
4. **Pick the words.** Use the source's own names. If a word means different things in two places, pick the most
   authoritative one (for code, the code) and tell the user.
5. **Write** the doc below. Next to the source for a codebase or local file; for a URL or anything else, ask where.
6. **Verify every name and example against the source.** One wrong term costs more trust than leaving it out.

## The doc

```markdown
# <Subject> — Vocabulary

## Where you are
**Above:** the purpose: <who it's for, what they get>.
**Here:** the parts, the rules and how they compose. Hold these in your head.
**Below:** the detail: <the code, the full post, the spec>. Go there only when changing one part.
Tags: **today** = in the source now · **planned** = not built or not settled.

## What it is
<2–3 sentences. Then the main flow as a one-line code block.>
**Does:** … · **Doesn't:** …

## <The N settings that shape every use>
<Only if they exist. Table: Question | Concept | Values. Say that they are independent.>

## The parts
<ASCII flow diagram: the parts and what passes between them. This is the map.>
<Table: Part | One job (one sentence). For a codebase, add a short Where column.>

## Design rules (use these to make judgement calls)
<5–8 numbered. Each: a bold, sharp claim someone could argue with, then one sentence of why, grounded in a real
detail from the source.>

## Ruled out
<Table: We don't… | Because. Only what someone would plausibly re-propose.>

## Don't confuse
<Optional, 3–5 rows. Table: These | Difference. Only real ambiguities, including one word used two ways.>

## The idea, reconstructed
<4–7 one-sentence bullets that rebuild the whole thing from the terms above, no new ones: the problem first, each
next bullet answering the gap the previous one left, the last one the outcome it serves. Read top to bottom they
make one argument: someone who reads only these should be able to explain it to someone else.>
```

## Taste

- **The first screen stands alone.** "Where you are" + "What it is" + the flow line give a correct, partial picture.
- **Sharp beats soft.** "The audio is the clock" is a decision. "Gives you leverage" is a description. Write
  decisions.
- **Never say the same thing twice.** If a section restates another, cut it. The reconstruction is the only
  summary.
- **Concrete beats abstract.** A real name, value or example from the source inside a rule beats a sentence
  explaining the rule.
- **Stay at altitude.** No internals, field lists, constants, recipes or hedges ("mostly", "originally"); no
  slogans the reader can't act on.
- **About three minutes to read, 60–120 lines.** Longer means it's becoming a manual, so cut.

## Updating

One living doc: new decisions amend it in place, never a new plan file. Keep the existing words, restructure into
the sections above rather than appending, and re-check every name against the source, since sources drift.
