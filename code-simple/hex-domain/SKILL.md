---
name: hex-domain
description: Manages the ubiquitous language and domain models for a Hexagonal Architecture project.
---

# Hexagonal Domain Modeler (hex-domain)

This skill takes established feature requirements and translates them into strict domain models and ubiquitous language definitions, without writing the actual code.

## The Workflow

### 1. Analyze Feature Specs
- Review the recently created/modified feature specs (e.g., in `docs/feature/domain/` or `docs/feature/adapters/`).

### 2. Evolve the Ubiquitous Language
- **`docs/language.md`**: Maintain and evolve the business language. Add or update canonical Things (nouns), Actions (verbs), and their relationships based on the feature.

### 3. Domain Modeling
Update or create the domain artifacts to navigate code-level decisions:
- **`docs/models/<domain-name>.md`**: 
  - Define the domain type system (only the core, important types).
  - Outline port interfaces (Inbound/Outbound) and the Service orchestration.
  - Detail any business state machines.
  - Ensure everything abides strictly by `docs/language.md`.

### 4. System Diagrams (Conditional)
- **`docs/mermaid.md`**: Update this system-wide asset ONLY when there is a structural change in domains (e.g., a new domain is introduced or a new cross-domain bridge is formed). Do not touch this for minor internal domain updates.

Once complete, the specifications are ready. Refer the user to the `hex-code` skill to implement the uncommitted changes in code.

## Reference Templates

When writing these documents, refer to the adapted templates bundled with this skill in the `templates/` directory:
- `language.md`
- `domain.md`
- `mermaid.md`
