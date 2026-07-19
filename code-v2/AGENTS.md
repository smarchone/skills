# Effective Working Guidelines — code-v2 (Hexagonal Architecture)

These are the operative rules for a codebase built and evolved with the **code-v2** skill pipeline.
They fold the repo-root hexagonal guidelines into v2's core idea: **snapshots hold state, feature
folders hold history, and `reconcile` keeps them honest.**

Read this before touching code or docs. When a rule here and a habit disagree, this file wins.

## 1. Project layout

```
<app>/
├── AGENTS.md                        # this file
├── docs/                            # the semantic layer
│   ├── business.md                  # SNAPSHOT: use cases + canonical vocabulary (one doc)
│   ├── mermaid.md                   # SNAPSHOT: single system-wide port diagram
│   ├── models/
│   │   └── <domain>.md              # SNAPSHOT: per-domain hexagonal sketch
│   └── features/
│       └── <name>/                  # HISTORY: one folder per feature
│           ├── feature.md           # the business-level delta (intent)
│           └── reconcile.md         # what changed when it met the code
├── cmd/
│   └── main.go                      # composition root (wiring)
└── internal/
    ├── core/                        # THE CORE (pure business models, services & ports)
    │   └── <domain>/                # one bounded context
    │       ├── model.go             # datatypes + business logic (rich models)
    │       ├── model_test.go        # invariant + pure-logic tests (in-memory)
    │       ├── ports.go             # inbound / sibling-inbound / outbound interfaces
    │       ├── service.go           # orchestration over ports
    │       ├── service_test.go      # orchestration tests (outbound ports mocked)
    │       └── context.md           # pointer back to docs/models/<domain>.md
    └── adapters/                    # THE OUTSIDE (mechanical; implementation details live here)
        ├── in/                      # inbound adapters: http/, event/
        └── out/                     # outbound adapters: db/, event/, thirdparty/
```

Each bounded context under `core/` owns its `model.go`, `model_test.go`, `ports.go`, `service.go`,
`service_test.go`, and `context.md`.

## 2. The docs are the semantic layer

- **`docs/business.md` and `docs/models/*` are snapshots** — they describe *what the system is now*,
  a faithful mirror of the code. They carry **no change-history** in their prose.
- **`docs/features/<name>/` is history** — `feature.md` is the business-level delta that drove a
  change; `reconcile.md` records what actually changed. This is where "added in feature X" lives.
- A reviewer should understand *what the system does* from `business.md` and *how it's structured*
  from `docs/models/*`, without reading Go. A snapshot that lies about the code is a bug — fix it.

## 3. Development guidelines (inside-out)

- **Develop the domain first** (creative, business-oriented); adapters come after (mechanical).
- **The snapshot binds the code at the level of business meaning, and no further.** Binding:
  **ports** (fully specified — they are the contract), **key types** (aggregate + vocabulary-bearing
  value objects), and **invariants**. Free: internal/incidental types (helper structs, private
  fields, internal enums) are the code's autonomy — design them idiomatically.
- **Vocabulary-driven.** Every core type/method traces to a canonical term in `docs/business.md`. If
  the code needs a term that isn't canonical, get it into `business.md` first — never invent domain
  vocabulary in code.
- **Enums are prefixed** (`TypeLimit`, not bare `Limit`) to avoid namespace clashes in a package.

## 4. Cross-domain calls (bridge pattern)

When Domain A needs a result from Domain B:
- Domain A defines an **outbound port** (interface in `domainA/ports.go`).
- A **bridge adapter** in `adapters/` implements that port and calls Domain B's inbound port (service).
- Domain A never imports Domain B — only the adapter knows both.
- Flow: `Domain A → A's outbound port → bridge adapter → B's inbound port (service) → Domain B`.

## 5. Anti-patterns

- **Anemic domain models.** Models that are just data holders with logic pushed to services. Build
  rich models (abstractions + composition); let services only stitch and orchestrate.
- **Snapshot as changelog.** Never accumulate "added in feature X" notes in `business.md` or
  `docs/models/*`. History belongs in `docs/features/<name>/`.
- **Implementation detail in the snapshots.** Concrete tech, wire formats, DB schemas, and adapter
  code belong to `internal/adapters/**` and the code — never to `business.md`, feature specs, or
  domain sketches.
- **Silent divergence.** Code and snapshot disagreeing without a `reconcile` pass. Reconcile, decide
  which is right, and re-sync.

## 6. Testing

- **`model_test.go`** — model invariants, domain actions, pure business logic. Fully in-memory; no
  external systems, no mocks.
- **`service_test.go`** — service coordination/orchestration. Mock the outbound ports from `ports.go`
  to isolate service behaviour.

## 7. The working loop

Each feature flows down; a code-touching session ends by flowing back up:

1. `feature-spec` → `docs/features/<name>/feature.md` — the business-level delta.
2. `business-spec` → fold the delta into `docs/business.md` (snapshot forward).
3. `domain-spec` → update the affected `docs/models/<domain>.md` and `docs/mermaid.md` (snapshot forward).
4. `domain-code` → evolve `internal/core/<domain>/` to match; run tests.
5. `reconcile` → re-sync the snapshots to the code, and record what changed + any process signals in
   `docs/features/<name>/reconcile.md`.

Adapters (`internal/adapters/**`) are **deferred** — generate them mechanically once the core is stable.
