# Hexagonal Architecture Agent Skills

This suite of modular AI agent skills manages and evolves a Golang Hexagonal Architecture project.

## Workflow

```text
/hex-feat          -->  /hex-domain        -->  /hex-code
(feature/product)       (language/domain)       (domain/adapter/wiring)
```

*(Use `/hex-drift` periodically to audit the codebase against the specs).*

## The Skill Toolchain

| Skill | Description | Templates |
|---|---|---|
| **`/hex-feat`** | Captures business requirements and updates product/feature specs without touching code. | `product.md`, `feature-name.md` |
| **`/hex-domain`** | Translates feature requirements into strict domain models and updates the ubiquitous language. | `language.md`, `domain.md`, `mermaid.md` |
| **`/hex-code`** | Reads uncommitted spec changes and implements the corresponding Golang code. | - |
| **`/hex-drift`** | Analyzes the codebase against documentation to report any architectural or vocabulary drift. | - |

*(Note: `hex-simple` is an older, monolithic version of this workflow).*

## TODO
- [ ] Add TDD (Test-Driven Development) approach to the workflow.
