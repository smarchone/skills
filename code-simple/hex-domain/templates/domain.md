# <Domain> — Domain Model Sketch

> Sketch only: type definitions and interface signatures. **No method bodies.**

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
service port is shown here

## Invariants
Enforced in the aggregate root, stated in canonical terms.
Every invariant names the error it returns — that error is how the rule is found from the code.

| Invariant | Error |
|---|---|
| <a **<Noun>** must always ...> | `Err<Condition>` |
| <**<verb>** is only permitted when ...> | `Err<Condition>` |

## Cross-domain interactions
Bridge pattern: this domain defines an outbound port; a bridge adapter implements it
and calls the sibling's inbound port. This domain never imports the sibling package.

| Outbound port here | Bridge adapter | Sibling inbound port |
|---|---|---|
| `<OutboundPort>` | `<Bridge>Adapter` | `<sibling>.<Domain>For<ThisDomain>` |

<or "none">

## Diagram
Maintained in `docs/mermaid.md` — this domain's subgraph plus its bridge edges.
