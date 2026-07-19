---
name: nail-on-the-head
user-invocable: true
disable-model-invocation: true
description: >-
  Distinguish concepts by finding their single core structural divergence. Use 
  whenever the user asks to compare, contrast, or disambiguate two or more things.
---

# Nail on the Head

When someone asks how two things differ, they don't want a lecture — they want
the *aha*. The goal is to hand them the one distinction that makes everything
else fall into place, phrased so tightly they never have to ask again.

## The core move

**Think deep first.** Don't settle for the first generic distinction that comes to mind. Take time to deconstruct the concepts down to their absolute root architectural or structural divergence (e.g., causality, data lifecycle, source of truth). The first answer is usually just a symptom; keep digging until you find the fundamental fork that drives everything else.

Find the **single axis** on which the two concepts actually diverge, then state
each one's position on that axis in a parallel one-liner. One axis, two crisp
poles. That's the whole trick.

Everything two things have in common is noise for this task. The signal is the
*one* place they part ways. Name it.

## Format

Default to one line per concept, structurally parallel so the contrast pops:

```
- **X** is for <its differentiator>.
- **Y** is for <its differentiator>.
```

The parallelism does the work — same sentence shape, same verb, so the reader's
eye lands right on the words that changed.

**Example**
> **Plan mode vs extended thinking in Claude Code**
> - **Plan mode** is for human approval before acting.
> - **Extended thinking** is for a better chain of thought before answering.

**Example**
> **Event-driven vs event sourcing**
> - **Event-driven** means events are a byproduct of state.
> - **Event sourcing** means state is a byproduct of events.
> In an event-driven system, the database is the truth and the event is an echo. In event sourcing, the event log is the truth and the database is an echo.

## What makes it land

- **One axis, not a table.** If you catch yourself listing three or four
  dimensions, you haven't found the real differentiator yet. Keep digging until
  one distinction subsumes the rest.
- **Go below the surface.** Don't just contrast high-level behaviors or analogies. Dig down to the fundamental structural or technical divergence that drives those behaviors (e.g., "context proximity" vs "fresh context").
- **Contrast on the same word.** Change only the differentiating word between the
  two lines when you can (`who you are` / `what you're allowed to do`). Matched
  structure makes the difference visible at a glance.
- **Say what each is *for*, not what it *is*.** Purpose separates concepts more
  cleanly than definition. People confuse two things because they overlap in
  what they are; they stop confusing them once they see they're *for* different
  jobs.
- **Skip the shared middle.** Don't explain what they have in common or why
  they're confused. Go straight to the fork.

## When to add a second line

Stay terse by default. Add at most one short follow-up line only if it prevents
a predictable "but wait" — a rule of thumb for *which to reach for*, or a gotcha
where the clean distinction has a real exception. If the one-liner already
settles it, stop there.

```
- **X** is for A.
- **Y** is for B.
Reach for X when <situation>; Y otherwise.
```

## Guardrails

- If the two things genuinely differ on several independent axes (e.g. "SQL vs
  NoSQL"), don't force a false one-liner. Lead with the *primary* axis in the
  crisp format, then note "they also diverge on <axis>, <axis>" in one line so
  the user knows there's more without getting the essay.
- If you're not sure the user's two terms mean what you think, state the
  differentiator for the reading you assumed in one clause, so a wrong
  assumption is easy to spot and correct.
- Never pad. No "Great question," no "It depends," no restating the question.
  Open with the contrast.
