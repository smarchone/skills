---
name: apply
description: Implements hexagonal Go domain code from docs/domain/* specs. Core only (no adapters/wiring).
---

# apply

The spec (`docs/domain/<domain>.md`) is the contract. Code realizes it exactly (same types, names, errors). If they disagree, the spec wins unless specified otherwise. Do not quietly "improve" the spec; raise issues if it looks wrong.

## Process

1. **Context First:** Read `docs/product.md`, `docs/language.md`, and the relevant `docs/feature/<name>.md` (if a feature name was provided) to ensure exact business vocabulary and intent are understood.
2. **Find Work:** Check `git status` and `git diff` for changes in `docs/domain/`. Only implement changed/untracked specs.
3. **Read Specs Fully:** Diff indicates where changes are, but you must read the full spec to understand implications (e.g. new methods, errors, tests).
4. **Halt on Conflict:** If code and spec conflict (e.g., dropped invariant, renamed type), stop and ask the user to resolve it. Do not guess.
5. **Write Core:** Implement `internal/<domain>/` (`model.go`, `ports.go`, `service.go`, and tests). Structure must strictly follow `AGENTS.md` or `CLAUDE.md`.
6. **Report:** List written files and explicitly flag any invariant that could not be cleanly expressed in code.

## Hexagonal Principles

Always read `AGENTS.md` or `CLAUDE.md` (if they exist in the project root) to infer the project's specific hexagonal architecture guidelines. At a baseline, adhere to the following:

- **Invariants in Aggregate Roots:** Protect state consistency. Enforce invariants inside the root. Unexport fields and use constructors if needed to prevent bypasses.
- **Pure Aggregates:** Only put rules in the aggregate if they require no I/O. Rules needing repository checks belong in the service. Never give a domain model a port.
- **Services Orchestrate:** Services load, call domain methods, save, and enforce cross-aggregate rules. Push logic down to the aggregate whenever possible.
- **No Sibling Imports:** A domain never imports another. Use outbound ports and bridge adapters for cross-domain calls.
- **Domain-centric Ports:** Name ports for what the domain needs (e.g., `OrderRepository`), not implementations.
- **Spec-matched Errors:** Define package-level `Err...` values matching the spec exactly.
- **No Adapters/Wiring:** Touch nothing outside `internal/<domain>/` unless explicitly asked.
