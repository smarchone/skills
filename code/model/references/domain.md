# <Domain> — Domain Spec

> Definitions only: types and interface signatures. **No method bodies.**

## Scope
<what this bounded context is responsible for, and explicitly what it is not>

**Aggregate root**: `<AggregateType>`

## Vocabulary → types
| Term | Type / method |
|---|---|
| **<Noun>** | `<GoType>` |
| **<verb>** | `<Aggregate>.<Method>()` |

**State machine:** <stateA → stateB → stateC, or "none">

## model.go (core)
```go
package <domain>
// value objects, aggregate, domain method signatures, errors
```

## ports.go
```go
package <domain>
// --- INBOUND: driving ---
// --- INBOUND: driven by siblings (via bridge) ---
// --- OUTBOUND: driven (persistence/publisher) ---
```
The driving port is the service contract, and the spec goes no further than that. Together with the Service rules below it fixes what each use case takes, returns, guarantees, and fails with — the orchestration behind it is the implementer's call, not something to sketch here.

## Invariants
Rules checkable from the aggregate's own state, with no I/O. Enforced in the aggregate root.
Every rule names the error it returns — that error is how it is found from the code.

| Invariant | Error |
|---|---|
| <a **<Noun>** must always ...> | `Err<Condition>` |
| <**<verb>** is only permitted when ...> | `Err<Condition>` |

## Service rules
Rules needing data the aggregate doesn't own — other aggregates, the caller, the request. Enforced in the service, before the domain call.

| Rule | Needs | Error |
|---|---|---|
| <a **<Noun>** may hold at most N open **<Noun>**> | <the port it loads from> | `Err<Condition>` |

## Cross-domain interactions
Bridge pattern: this domain defines an outbound port; a bridge adapter implements it
and calls the sibling's inbound port. This domain never imports the sibling package.

| Outbound port here | Bridge adapter | Sibling inbound port |
|---|---|---|
| `<OutboundPort>` | `<Bridge>Adapter` | `<sibling>.<Domain>For<ThisDomain>` |

<or "none">

## Wiring
What `cmd/main.go` constructs for this domain:
- `<Aggregate>Repository` ← `<adapter implementation>`
- `<Domain>Service` ← core service, wired with the ports above
- `<OutboundPort>` ← `<Bridge>Adapter{<sibling service>}`

## Diagram
Maintained in `mermaid.md` — this domain's subgraph plus its bridge edges.
