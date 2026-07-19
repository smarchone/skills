---
name: domain-spec
user-invocable: true
disable-model-invocation: true
description: 'Maintain the domain-structure snapshot bridging docs/business.md to code — hexagonal model sketches (complete ports, key types, no bodies) at docs/models/<domain>.md, kept current with docs/mermaid.md.'
---

# domain-spec

The **bridge** between the business spec and the code. Translate `docs/business.md` into hexagonal
model sketches — aggregate/value types, inbound/outbound ports, invariants, cross-domain interactions —
with **no implementations**. As features land, *evolve* the affected domain sketch(es) rather than
regenerating everything, and keep the single shared `docs/mermaid.md` current.

Together with `docs/business.md`, these sketches are the **semantic layer** over the core code:
they say what each domain is and how domains connect, so the code can be read against them.

Each domain sketch is a **snapshot of the codebase's domain structure** — it always mirrors the ports,
key types, and invariants that exist in the code *now*. It is not a changelog; the history of what
changed lives in the feature folders. `reconcile` is what keeps this snapshot true to the code.

## Principles (the taste)
- **Complete ports, key types only.** Ports are the contract — the seams between domains, the bridges,
  the outside world — so specify them *fully and precisely*. Types are sketched at the level of
  *business meaning*: the aggregate root and the vocabulary-bearing value objects only. Leave internal
  and incidental types (helper structs, private fields, internal enums) to the code layer's autonomy.
- **No bodies.** Type definitions and interface signatures only — never method implementations.
- **Two guardrails on that autonomy.** Every canonical term in the `vocabulary → types` mapping must
  have a named type here (those *are* the key types), and every invariant must be stated even if the
  type that enforces it is only sketched.
- **Vocabulary-driven.** Every type and method maps to a canonical term in `docs/business.md`.
  If a sketch needs a term that isn't canonical, stop and get it into business.md first — don't
  invent domain vocabulary here. If business.md renamed a term, cascade the rename into the sketch.
- **Inside-out.** Model the core (aggregate + value objects + behaviour) before the ports.
- **Invariants live in the aggregate root.** Not in services, not in adapters.
- **Port roles are explicit.** Split inbound (driving), inbound (driven by siblings via bridge),
  and outbound (persistence/publishers).
- **No identifier collisions.** Prefix enums (`TypeLimit`, not bare `Limit`).
- **Cross-domain via bridge.** Domain A defines an outbound port; a bridge adapter implements it and
  calls Domain B's inbound port. Domain A never imports Domain B.
- **Evolve, don't rewrite.** For an incoming feature, touch only the domains it affects; note new
  vs changed elements.

## Process
1. Read `docs/business.md`. If evolving for a feature, read the relevant `docs/features/<name>/feature.md`.
2. Determine which bounded context(s) the change touches — or, on a fresh system, infer the full set
   from clusters of Things/Actions/Relationships.
3. For each affected domain:
   a. Confirm the aggregate root and the `vocabulary → types` mapping.
   b. Update `model.go` sketch (value objects, aggregate, domain method signatures, errors).
   c. Update `ports.go` sketch (inbound driving, sibling-inbound, outbound).
   d. Update invariants and cross-domain interactions.
   e. Write `docs/models/<domain>.md`.
4. Update `docs/mermaid.md` — add/refresh this domain's subgraph and bridge edges. Follow
   `mermaid-diagram.md` in this skill for conventions. Never create per-domain diagram copies.

## Output template (`docs/models/<domain>.md`)

```markdown
# <Domain> — domain-model sketch

## Scope
<what this bounded context owns, one paragraph>

## Vocabulary → types
| Term | Type / method |
|---|---|
| **<Term>** | `<GoType / method>` |

**State machine:** <lifecycle, or "none">

## model.go (core)
```go
package <domain>
// KEY types only: aggregate root + vocabulary-bearing value objects,
// domain method signatures, domain errors — no bodies.
// Internal/incidental types are left to the code layer.
```

## ports.go
```go
package <domain>
// --- INBOUND: driving ---
// --- INBOUND: driven by siblings (via bridge) ---
// --- OUTBOUND: driven (persistence / publisher) ---
```

## Invariants
- <invariant in canonical terms — enforced in the aggregate root>

## Cross-domain interactions
<bridge flows: Domain A → outbound port → bridge adapter → Domain B inbound port; or "none">

## Wiring
<what cmd/main.go will need to construct>
```

## Hand-off
`docs/models/<domain>.md` + `docs/mermaid.md` are the input to `domain-code`. Do not implement code
here. If a needed term is missing from `docs/business.md`, get it added there before sketching.
