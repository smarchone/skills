# code-v2 — a feature-driven spec→code harness

A skill system for building and **evolving** a hexagonal-architecture codebase one feature at a time.

Two kinds of doc, and the distinction runs through everything:
- **Snapshots** — `business.md` + the domain specs — describe *what the system is now*. They are a
  semantic mirror of the codebase: read them to understand the system without reading Go.
- **History** — the `docs/features/<name>/` folders — describe *what changed and why*. Each feature is
  a business-level delta plus the record of what reconciling it against the code produced.

Build flows down (feature → snapshots → code). `reconcile` flows back up: it re-syncs the snapshots to
the code and writes the change record into the feature folder.

## The pipeline

```
         ┌──────────────────────── downward: build ────────────────────────►
feature  ──►  business.md  ──►  domain spec  ──►  core domain code
(a change)    (single spec:      (docs/models/*    (Go, hexagonal —
              use cases +         + mermaid.md)      per AGENTS.md)
              canonical vocab)                      [ adapter spec — deferred ]
         ◄──────────────── upward: reconcile drift ───────────────────────┘
              (docs/features/<name>/reconcile.md — seeds self-improvement)
```

| Layer | Skill | Artifact | Role |
|---|---|---|---|
| Layer | Skill | Artifact | Kind | Role |
|---|---|---|---|---|
| Feature | `feature-spec` | `docs/features/<name>/feature.md` | history | The **business-level delta** — only what changes in `business.md`. No domain design, no implementation. Each feature is a **folder**. |
| Business | `business-spec` | `docs/business.md` | snapshot | The **single** business snapshot: use cases + canonical vocabulary in one place. |
| Domain | `domain-spec` | `docs/models/<domain>.md`, `docs/mermaid.md` | snapshot | Domain-structure snapshot bridging business → code. Complete ports, key types. |
| Code | `domain-code` | `internal/core/<domain>/*.go` | code | The core domain code. |
| Reconcile | `reconcile` | `docs/features/<name>/reconcile.md` | history | Re-syncs the snapshots to the code; records what changed, beside the feature that caused it. |
| Adapter | *(deferred)* | `internal/adapters/**` | code | Purely mechanical; port implementations. **Where implementation details live.** Evolve later. |

## What's different from v1 (`code/`)

- **There is now a feature layer.** v1 was a one-shot waterfall (all business → all vocab → all domains). v2 is **incremental**: each feature flows down the pipeline and the artifacts below it *evolve* rather than being regenerated from scratch.
- **Business and vocabulary are one spec.** v1 split `business.md` and `vocab.md`; v2 merges them into a single `docs/business.md` so the language and the use cases can never drift apart.
- **Adapters are explicitly deferred.** They're mechanical and can be generated once the core is stable.

## The semantic layer (snapshots)

`business.md` + the domain specs are **snapshots** that sit above the code as its meaning. A reviewer
should be able to understand *what the system does* from `business.md` and *how it's structured* from
the domain specs, without reading Go. When code and a snapshot disagree, `reconcile` decides which is
right and re-syncs — a snapshot must never be left lying about the code.

They bind the code at the level of **business meaning, and no further**: ports, key types
(aggregate + vocabulary-bearing value objects), and invariants are binding; internal/incidental types
are the code layer's autonomy, and concrete implementation details belong to the adapter/code layers —
never to the snapshots. This keeps the semantic layer stable and readable while leaving the
implementation free to be idiomatic.

**Discovery/research happens in the feature layer**; every layer below only *consolidates*. Features may
*propose* vocabulary or use-case changes, but the **business layer owns the language** — once a term
changes there, the rename **cascades** down through domain spec and code.

Building flows down; **reconciliation is the one deliberate upward flow.** After a session,
`reconcile` compares the code to the snapshots and syncs legitimate drift back up (or fixes code that
diverged by accident) — only across the *binding surface* (ports, key types, invariants, vocabulary,
use cases), never the code's autonomy zone — and records what changed in the feature folder. Every
unspecified decision the code was forced to make is logged there as a *process signal*: the raw
material for a future self-improving loop that tightens these skills where drift keeps recurring.

## Working loop

For each new feature, run the skills top-to-bottom, stopping for human review between layers:

1. `feature-spec` — refine the raw ask into `docs/features/<name>/feature.md`; surface any new vocabulary.
2. `business-spec` — fold the feature into `docs/business.md`, keeping vocabulary consistent.
3. `domain-spec` — update the affected domain sketch(es) and `docs/mermaid.md`.
4. `domain-code` — evolve the Go core to match the updated sketch.
5. `reconcile` — after the session, re-sync the snapshots to the code and record what changed.

Steps 1–4 flow **down** (build); step 5 flows **up** (reconcile). Each layer only touches its own
artifact and hands off to the next. A change can stop early (e.g. a snapshot-only refinement) — you
don't have to run the whole chain every time — but any session that *touched code* ends with
`reconcile`, because that's the only step that keeps the snapshots honest.

## Target architecture

Go hexagonal (core domains + ports; adapters implement ports; cross-domain calls via the bridge
pattern). The effective, v2-aware working rules live in **`AGENTS.md`** in this folder — it folds the
repo-root hexagonal guidelines into the snapshot/history model and doubles as the `AGENTS.md` to drop
into a generated code-v2 project's root. This is the starting target and will evolve.

## A note on structure

These templates are **starting points, not contracts**. Keep the specs as light as the system
currently warrants; add sections only when a real feature earns them. Structure is extracted from
usage, not predicted up front.
