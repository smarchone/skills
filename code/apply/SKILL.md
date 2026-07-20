---
name: apply
description: Implement or update hexagonal Go domain code from the specs in docs/domain/. Writes internal/<domain>/ to match the spec — model.go, ports.go, service.go, and tests. Use when the user wants domain code, services, or use cases written or reconciled with the spec ("implement the domain", "write the service for X", "make the code match the spec"), and after an approved /update-spec. Core only — not adapters, handlers, or storage.
---

# apply

The spec in `docs/domain/<domain>.md` is the contract. Code realises it — same types, same names, same errors. Where the two disagree, the spec wins unless the user says otherwise.

The spec is also a decision the user already reviewed. They shaped the code's direction there, while it was still cheap to change — which is why implementing it faithfully matters more than improving on it. If the spec looks wrong, say so rather than quietly building something better.

## Process

1. **Load the mental model.** Read `docs/product.md` and `docs/language.md` before anything else. They carry what the business is doing and the exact words for it — without them you will invent a synonym or name a type after the wrong concept, and nothing downstream will catch it.

2. **Find the work list.** `git status --short docs/domain/` and `git diff HEAD -- docs/domain/ docs/language.md`. Changed or untracked specs are what `/update-spec` proposed and the user approved. If nothing changed, ask what to implement rather than regenerating every domain.

3. **Read each changed spec in full.** The diff scopes the work; it doesn't specify it. A one-line change to an invariant can imply a new method, a new error, and a new test.

4. **Stop on any conflict between spec and code.** A renamed type, a dropped invariant, an extra method, a changed signature — raise it and let the user resolve it. Don't pick a winner, don't reconcile it yourself, don't proceed with the rest and mention it afterwards. Either side may be the one that's right: the code can hold a decision nobody wrote down, and the spec is a decision the user made deliberately. Only they know which.

5. **Write the core** into `internal/<domain>/` — `model.go`, `ports.go`, `service.go`, `model_test.go`, `service_test.go`. Layout and skeletons in `references/go-layout.md`.

6. **Report** the files written, plus any invariant you could not express in code. That gap is worth more to the user than a test that pretends to cover it.

## What makes it hexagonal

- **Invariants live in the aggregate root.** The aggregate is a consistency boundary: if every mutation goes through the root, the root is the one place that can guarantee the rule still holds afterwards. Put it in the service instead and the guarantee weakens to "holds if you came through the right door" — a second caller, or a directly constructed struct, and it's silently gone. If a rule can be bypassed by building the struct, unexport the fields and enforce it in a constructor.

- **But only rules the aggregate can actually check.** Ask: can this be verified from the aggregate's own state, with no I/O? If yes it's an invariant — put it in the root, where it tests with no mocks at all. If it needs a repository call, it isn't an invariant. "A **Customer** may hold at most 3 open **Orders**" needs data this aggregate doesn't own, and so does any rule about who the caller is. Those belong in the service. Forcing them into the root means handing the domain a port, which is the coupling this architecture exists to prevent.

- **The service orchestrates; it doesn't decide.** It loads through ports, calls domain methods, saves, publishes, and enforces the cross-aggregate and policy rules it has the data for. Business logic that *could* live in the aggregate should — a service that starts making state-shape decisions is how domains turn anaemic.

- **A domain never imports a sibling domain.** Cross-domain calls leave through an outbound port declared here and implemented by a bridge adapter elsewhere. If you find yourself reaching for another domain's package, the spec needs an outbound port — say so rather than adding the import.

- **Ports are named for what this domain needs**, not for what will implement them: `OrderRepository`, never `PostgresOrders`. The core must read the same regardless of what gets plugged in.

- **Errors are package-level `Err…` values** matching the spec exactly. They are how a reader gets from a line of code back to the business rule that put it there — which is also why every invariant in the spec names one.

- **No adapters, no `cmd/main.go` wiring** unless asked. Specs list wiring so a human can do it deliberately.

## Scope

`internal/<domain>/` only. Transport, storage, and adapters are a separate job.
