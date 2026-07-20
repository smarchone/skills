---
name: update-spec
description: Model features into a project's snapshots — rewrites docs/product.md, docs/language.md, and docs/domain/*.md to describe the business as it now stands. Creates product.md and language.md if missing, so this is also how a project's model starts. Use after /feature, or whenever the user wants the product, vocabulary, or domain specs brought up to date ("update the model", "rebuild the snapshots", "the vocabulary is out of date"). Docs only; /domain turns the specs into code.
---

# update-spec

Features are the log; the snapshots are what you model out of them. This skill runs that modelling.

| Snapshot | Is a function of | Changes |
|---|---|---|
| `docs/product.md` | all features | often, in small increments |
| `docs/language.md` | all features | rarely, and never casually |
| `docs/domain/<domain>.md` | features touching that context | with each feature that lands in it |

A snapshot is the business as it now stands — not a per-feature appendix and not a running list of amendments. So a new feature can force a rewrite of something an old feature established. When it does, that is a finding worth reporting, not a conflict to smooth over.

## Scope of a run

Two modes, and it matters which you're in:

- **Incremental** — one confirmed feature just landed. Read it, read the current snapshots, and fold it in. This is the common case.
- **Full remodel** — the user wants the snapshots rebuilt from `docs/feature/` as a whole. Read every feature. Expect to find terms that drifted, scope bullets describing features later superseded, and domain specs that no longer partition cleanly. Report what you reconciled.

If the user hasn't said which, infer from what they asked for and say which mode you're in before you start.

## Process

1. **Read the features.** The new one, or all of them. Their New terms tables are the raw input to `language.md` — including the "why not an existing term" column, which tells you what was already considered and rejected so you don't reopen it.

2. **Update `language.md` first.** Everything downstream is phrased in it, so settling the words first avoids rewriting the same sentence in three files. Add terms only when the concept is genuinely new; a synonym admitted here breaks the term→code mapping everywhere and nothing catches it later. If a feature's new term duplicates an existing one, keep the existing one and say so.

3. **Update `product.md`** — scope bullets, and any risk or assumption the features exposed.

4. **Update the domain specs.** Assign each feature's rules to the context that owns them. Propose a **new domain** when a feature's terms cluster away from every existing context — say what the cluster is and why it doesn't fit, and let the user settle it rather than creating it silently. A new bounded context is a structural commitment.

5. **Refresh the diagram.** Update `docs/domain/mermaid.md` so it matches the specs — a subgraph per domain with its ports, plus an edge per bridge. It is one shared file covering the whole system, never a diagram per domain. Conventions in `references/mermaid.md`.

6. **Report briefly** — files touched, one line each; any term you rejected and why; anything a feature demanded that the current model can't express.

## The proposal mechanism

Write the edits directly and **leave them uncommitted**. The working tree *is* the proposal — the user reviews it with their own diff tooling, and their suggestions come back as revisions to the same uncommitted files.

That is why this skill doesn't ask permission edit-by-edit or narrate at length. Make the edits, say what changed and why in a few lines, and let the diff carry the detail.

## Taste

- **Be reluctant with `language.md`.** It is the most expensive file to change, because every domain spec and every line of domain code is phrased in it. A term added here is a commitment; a term renamed here is a migration.

- **Don't let a snapshot become a changelog.** They describe the business as it is now. If a new feature supersedes an old one, rewrite the affected passage rather than appending a caveat to it — the feature files already hold the history.

- **Say what you couldn't fit.** A feature rule that has no natural home in any domain spec is telling you something about the model. Surface it instead of forcing it into the nearest context.

## Output formats

| Doc | Format |
|---|---|
| `docs/product.md` | `references/product.md` |
| `docs/language.md` | `references/language.md` |
| `docs/domain/<domain>.md` | `references/domain.md` |
| `docs/domain/mermaid.md` | `references/mermaid.md` |

## Hand-off

Docs only — write no code. `/domain` implements the approved domain specs.
