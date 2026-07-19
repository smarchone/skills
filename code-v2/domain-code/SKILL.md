---
name: domain-code
user-invocable: true
disable-model-invocation: true
description: 'Generate and evolve the Go hexagonal core domain code (model.go, ports.go, service.go + tests) from the domain snapshot docs/models/<domain>.md, keeping code faithful to the snapshots. Adapters are deferred.'
---

# domain-code

Turn a domain sketch (`docs/models/<domain>.md`) into working **core domain code**, and evolve it as
features land. The specs (`docs/business.md` + the domain sketch) are the semantic layer — the code
must remain a faithful realisation of them. Target: Go hexagonal per `AGENTS.md`.

**Scope: core only.** Generate `internal/core/<domain>/`. Adapters (`internal/adapters/**`) are
mechanical and deferred — do not generate them unless explicitly asked.

## Principles (the taste)
- **Faithful to the specs — and free within them.** Ports, key types (aggregate + vocabulary-bearing
  value objects), and invariants are *binding*: implement them exactly as the sketch defines. But the
  sketch deliberately stops there — internal and incidental types (helper structs, private fields,
  internal enums) are **yours to design**. Use that autonomy for clean, idiomatic Go.
- **Never diverge the binding parts.** If the code wants a port, key type, or invariant the specs don't
  have, stop and fix the spec first — never let the semantic layer and the code drift apart silently.
- **Rich domain, not anemic.** Business logic and invariants live in the model (aggregate root) with
  real behaviour and composition. Services only stitch and orchestrate ports.
- **Ports are interfaces.** Inbound (driving), sibling-inbound, and outbound ports as defined in the
  sketch. Cross-domain calls go through the bridge pattern — a domain never imports a sibling.
- **Test the core in-memory.** `model_test.go` for invariants and pure logic (no mocks, no I/O);
  `service_test.go` for orchestration (mock outbound ports).
- **Evolve, don't regenerate.** For a feature, change only what the updated sketch changed. Preserve
  existing tests; add tests for new behaviour.

## Layout (per `AGENTS.md`)
```
internal/core/<domain>/
├── model.go        # value objects, aggregate, business logic, errors
├── model_test.go   # invariant + pure-logic tests (in-memory)
├── ports.go        # inbound / sibling-inbound / outbound interfaces
├── service.go      # orchestration over ports
├── service_test.go # orchestration tests (outbound ports mocked)
└── context.md      # short pointer back to docs/models/<domain>.md
```

## Process
1. Read `docs/models/<domain>.md` (and `docs/business.md` for term meanings). If evolving, read the
   incoming `docs/features/<name>/feature.md`.
2. Implement/update `model.go`: value objects, aggregate with real methods, invariants enforced in the
   aggregate root, domain errors.
3. Implement/update `ports.go`: interfaces exactly as sketched.
4. Implement/update `service.go`: orchestration only; depend on ports, not concretions.
5. Write/extend `model_test.go` and `service_test.go`.
6. Add `context.md` pointing to the sketch. Build + run tests; report results honestly.
7. Set the feature's `status:` to `implemented` in its feature file and in the business.md feature index.

## Verifying against the semantic layer
Before finishing, check the round-trip: does every canonical term in the domain's `vocabulary → types`
mapping appear in code, and does every code type/port trace back to a term? Report drift — a mismatch
means either the code or the spec is wrong, and it must be reconciled, not ignored.

## Hand-off
Core code lives under `internal/core/<domain>/`. Adapters remain deferred; when the core is stable and
the user asks, a future adapter skill implements the ports in `internal/adapters/**`.
