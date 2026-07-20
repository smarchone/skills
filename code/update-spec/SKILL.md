---
name: update-spec
description: Models features into project snapshots (product.md, language.md, domain specs). Updates the business model based on confirmed features. Creates these files if missing. Docs only; /domain turns specs into code.
---

# update-spec

Features act as an append-only log; snapshots reflect the current state of the business modeled from them.
New features often require rewriting old established rules in snapshots—this is expected.

## Scope of a Run

Determine and state your mode before starting:
- **Incremental:** A new feature just landed. Fold it into the existing snapshots.
- **Full Remodel:** Rebuild snapshots from all files in `docs/feature/`. Reconcile drifted terms and superseded scope.

## Process

1. **Read Features:** Review the relevant feature(s), paying special attention to proposed vocabulary changes.
2. **Update `language.md` First:** Resolve vocabulary before anything else. Be strict: only add genuinely new concepts. Reject synonyms and flag duplicates.
3. **Update `product.md`:** Update scope, vision, risks, and assumptions based on the features. Explicitly link to the relevant feature specs (`docs/feature/<name>.md`) in the scope sections.
4. **Update Domain Specs (`docs/domain/*.md`):** Assign rules to their owning contexts. If rules don't fit anywhere, propose a **new domain** and explain why; do not create it silently.
5. **Update Diagram:** Refresh `docs/domain/mermaid.md` to match the specs (one shared file for the whole system, using `references/mermaid.md`).
6. **Report:** Briefly list files touched, rejected terms, and any un-modellable feature requirements.

## Guidelines

- **Propose via working tree:** Write edits directly and leave them uncommitted. The diff is the proposal. Do not ask for permission edit-by-edit.
- **Protect `language.md`:** It's the most expensive file to change. Adding a term is a commitment; renaming is a migration.
- **Snapshots are not changelogs:** Rewrite superseded passages entirely instead of appending caveats. The history lives in the feature files.
- **Highlight misfits:** If a rule has no natural home, surface it instead of forcing it into an unrelated domain.

## Output Formats

| Doc | Template |
|---|---|
| `docs/product.md` | `references/product.md` |
| `docs/language.md` | `references/language.md` |
| `docs/domain/<domain>.md` | `references/domain.md` |
| `docs/domain/mermaid.md` | `references/mermaid.md` |

## Hand-off
Write **no code**. Once specs are approved, the `/domain` skill implements them.
