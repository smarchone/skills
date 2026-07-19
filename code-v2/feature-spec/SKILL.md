---
name: feature-spec
user-invocable: true
disable-model-invocation: true
description: 'Capture a feature as a business-level delta at docs/features/<name>/feature.md — only what changes in business.md (use cases + vocabulary). The history entry that drives the code-v2 pipeline.'
---

# feature-spec

Capture **one unit of change** as `docs/features/<name>/feature.md`. Each feature is a **folder**:
`feature.md` holds the intent (this skill), and `reconcile.md` will later hold what actually changed
for that feature (written by `reconcile`).

**A feature spec describes only the change to `business.md`** — new/changed use cases and vocabulary.
It is the *delta* to the business snapshot. It does **not** describe domain structure (that's the
domain snapshot's job) or implementation/adapter details (those live in the code and adapter layers).
The feature folder is the system's history of *what changed and why*; the specs are the current
snapshot of *what is*.

## Principles (the taste)
- **One feature, one folder.** A feature is the smallest coherent change worth naming. If the ask
  bundles several, split it and say so.
- **This is where research happens.** The feature layer owns *discovery* — how this thing is normally
  done, domain conventions, edge cases, candidate terminology (use `WebSearch` when it helps). New
  information enters the system here; downstream layers consolidate, they don't re-discover.
- **Speak the existing language.** If `docs/business.md` exists, reuse its canonical vocabulary
  verbatim. Any *new* noun/verb the feature needs is flagged explicitly for promotion — don't
  silently invent synonyms for concepts that already have a canonical term.
- **Features propose, they don't decide.** A feature may reveal that an existing canonical term is
  wrong/too narrow, or that a use case needs reframing. Record that as a *proposal* — the authority to
  change `business.md` lives in the business layer, human-in-the-loop.
- **Only `business.md` changes.** Describe behaviour and value at the business level. No domain design
  (types, ports, aggregates) and no implementation/adapter details — those belong to the domain snapshot
  and the code/adapter layers, not here.
- **Human-in-the-loop.** Ask pointed clarifying questions before writing. Don't assume the goal.
- **Light by default.** Fill only the sections the feature actually needs. Delete the rest.

## Process
1. Read the raw request. If `docs/business.md` exists, read its vocabulary and use cases first.
2. Research the feature: how it's conventionally done, terminology, the edges that matter.
3. Clarify with the USER: intent, actors, the happy path, the edges, what's explicitly out.
   Use `AskUserQuestion` when a few crisp choices would resolve ambiguity faster than prose.
4. Map the feature onto existing vocabulary: terms it reuses, terms it *introduces*, and any changes
   it *proposes* to existing terms or use cases.
5. Name the feature (`kebab-case`, verb-led where natural, e.g. `apply-discount-code`).
6. Create the folder `docs/features/<name>/` and write `feature.md` in it from the template.
7. Hand off to `business-spec` — the feature spec's only downstream consumer.

## Output template (`docs/features/<name>/feature.md`)

```markdown
# Feature: <human title>

- **id:** <kebab-case-name>
- **status:** proposed        <!-- proposed → specced → implemented -->

## Intent
<one or two sentences: what becomes possible, and why it matters>

## Scenarios
- <actor> <does something> so that <outcome> — written in canonical vocabulary.
- <the edge cases that change behaviour>

## Vocabulary
- **Reuses:** <existing canonical terms this feature touches>
- **Introduces:** <new nouns/verbs to promote into business.md — or "none">

## Proposes changes
<changes this feature suggests to existing business.md — a term to rename/broaden, a use case to
reframe. Proposals only; business-spec adjudicates. "none" if it fits the current model as-is.>

## Out of scope
- <what this feature deliberately does not do — at the business level>
```

## Hand-off
`docs/features/<name>/feature.md` is the input to `business-spec`. Do **not** edit `docs/business.md`,
domain sketches, or code from here — feature-spec only produces the feature file.
