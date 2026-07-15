---
name: hex-domain
description: 'Infer bounded contexts from docs/vocab.md and produce hexagonal domain-model sketches for ALL domains (datatypes + interfaces only).'
---

# Hex Domain Model

Infer the list of all possible domains (bounded contexts) from `docs/vocab.md` and generate a **hexagonal model sketch** for **every** domain: aggregate/value types, inbound/outbound ports, invariants, and cross-domain interactions via bridges. 
**No implementations**. Update the single shared `docs/mermaid.md` with all domains' ports.

## Principles (The Taste)
- **Sketch only:** Type definitions and interface signatures only. No method bodies.
- **Inside-out:** Model the core (aggregate + value objects + behaviour) before ports.
- **Vocabulary-driven:** Map every type/method strictly to `docs/vocab.md`.
- **Vocabulary updates:** If the vocabulary needs to be changed, ask for permission before changing it directly. If permitted after review, update `docs/vocab.md` as well.
- **No identifier collisions:** Prefix enums (`TypeLimit`, not bare `Limit`) to avoid namespace clashes within the package.
- **Port roles:** Split inbound (driving), inbound (driven by siblings), and outbound (driven/persistence).
- **Invariants:** Must live in the aggregate root.
- **Cross-domain calls (Bridge Pattern):** Domain A defines an outbound port, a bridge adapter implements it and calls Domain B's inbound port. Domain A never imports Domain B.

## Process
1. Read `docs/vocab.md` and infer the list of bounded contexts (domains) based on the clusters of Things, Actions, and their Relationships.
2. For **every** domain inferred, repeat steps 3-8:
3. Name the bounded context and identify its aggregate root.
4. Build the `Vocabulary → types` mapping for this domain.
5. Sketch `model.go` (value objects, aggregate, pure domain methods, errors).
6. Derive `ports.go` (inbound, sibling-inbound, outbound).
7. List invariants and describe cross-domain interactions.
8. Write the sketch to `docs/models/{{domain}}.md`.
9. Update `docs/mermaid.md` (add or refresh subgraphs for all domains). Refer to `mermaid-diagram.md` in this skill for the diagram format and conventions.

## Output Template (`docs/models/{{domain}}.md`)

```markdown
# <Domain> — Domain Model Sketch

## Scope
<brief description>

## Vocabulary → types
| Term | Type / method |
|---|---|
| **<Term>** | `<GoType / method>` |

**State machine:** <lifecycle or "none">

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

## Invariants
- <invariant in canonical terms>

## Cross-domain interactions
<bridge pattern flows or "none">

## Wiring
<what cmd/main.go constructs>

## Diagram
Updated in `../mermaid.md`. (See `mermaid-diagram.md` in this skill for formatting conventions).

## Hand-off
Write the file, then update `docs/mermaid.md` following the formatting conventions in `mermaid-diagram.md`. Do not implement the code unless requested.
