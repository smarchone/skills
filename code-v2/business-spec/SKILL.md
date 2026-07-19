---
name: business-spec
user-invocable: true
disable-model-invocation: true
description: 'Fold a feature delta into docs/business.md — the single business snapshot holding use cases AND canonical vocabulary together. Keeps the snapshot current and enforces one word per concept as the system evolves.'
---

# business-spec

Maintain `docs/business.md`: the **single** semantic business spec for the system. It holds the
canonical vocabulary and the use cases *in one document* so the language and the behaviour can never
drift apart. This skill **evolves** the doc as features land — it is rarely written from scratch.

`docs/business.md` is a **snapshot of the codebase's business semantics** — it always describes *what
the system does now*, not how it got there. The history of changes lives in the feature folders; this
doc is only ever the current state. Applying a feature's delta here moves the snapshot forward.

## Principles (the taste)
- **A snapshot, not a log.** Describe the current system. Never accumulate change-history or "added in
  feature X" notes in the prose — the feature folders are the history. The only nod to history is the
  feature index at the bottom.
- **One spec.** Vocabulary and use cases live together here. There is no separate `vocab.md` in v2.
- **One word per concept, one concept per word.** Ban synonyms (say "lock", never "hold"); disambiguate
  homonyms. Prefer common industry terms over clever ones. Separate Things (nouns) from Actions (verbs).
- **Fold, don't append.** A new feature integrates into the existing vision, vocabulary, and scenarios —
  it doesn't get bolted on as a disconnected section. Reconcile conflicts with existing terms explicitly.
- **New vocabulary is a decision.** When a feature introduces a term, either promote it into the
  canonical vocabulary or map it onto an existing term. Surface the choice to the USER; don't guess.
- **Consolidate, don't discover.** Research/discovery happened in the feature layer. Here you only
  *canonicalize* — pick the industry-standard term from what the feature surfaced ("common over clever").
- **This layer owns the language.** Features *propose* changes to existing terms or use cases; this is
  where they're adjudicated (with the USER). Once a term changes here, that change is authoritative and
  must cascade downstream — flag it so domain-spec and domain-code follow the rename.
- **Purely business.** No types, ports, or code. This is the *what*, not the *how*.
- **Human-in-the-loop.** Present vocabulary changes and scope shifts for confirmation before writing.

## Process
1. Read the incoming `docs/features/<name>/feature.md` (its *Introduces* and *Proposes changes* sections) and
   the current `docs/business.md` (if any).
2. Reconcile vocabulary: for each introduced term decide promote-or-map; for each proposed change
   decide accept/reject/amend. Confirm with the USER.
3. Fold the feature's scenarios into the use cases, rewritten strictly in canonical terms.
4. Update scope, lifecycles, relationships, and risks as the feature requires.
5. Mark the feature in the feature index; set its `status:` to `specced` in the feature file.
6. Write `docs/business.md`. If any term changed, note the rename so downstream layers can cascade it.

## Output template (`docs/business.md`)

```markdown
# Business Spec

## Vision
<the boiled-down intent of the whole system, in first-principles business terms>

## Canonical vocabulary

### Things (nouns)
| Term | Meaning | Banned synonyms |
|---|---|---|
| **<Noun>** | <one line> | <banned> |

### Actions (verbs)
| Verb | Meaning | Banned synonyms |
|---|---|---|
| **<verb>** | <one line> | <banned> |

### Relationships
| From | Relationship | To | Note |
|---|---|---|---|
| **<Thing>** | owns / has-many / references | **<Thing>** | <one line> |

### Lifecycles
- **<Thing>**: <stateA> → <stateB> — <verb that triggers the transition>.

## Use cases
Each written using **only** canonical vocabulary (terms in bold).
- **<Use case>** — <actor> **<verb>**s a **<Thing>** so that <outcome>; <key edges>.

## Scope
- **In:** <bounded set of what the system does>
- **Out:** <explicitly excluded>

## Risks & assumptions
- <gaps, adversarial concerns, implicit assumptions and their mitigations>

## Features folded in
| Feature | Status | Notes |
|---|---|---|
| `<feature-id>` | specced / implemented | <what it added/changed> |
```

## Hand-off
`docs/business.md` is the input to `domain-spec`. Do not touch domain sketches or code from here.
When vocabulary changes, that change is authoritative downstream — flag it so domain-spec and
domain-code can follow.
