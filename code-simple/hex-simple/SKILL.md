---
name: hex-simple
description: Orchestrates a workflow to create reviewable specs and domain artifacts for a Golang Hexagonal Architecture project.
---

# Hexagonal Domain Spec Generator

This skill helps manage a project by accumulating features and translating them into robust, reviewable domain specifications for a Golang Hexagonal Architecture codebase.

## Overview
A Hexagonal Golang codebase consists of:
1. **Domain (The Core)**: Business use cases, state machines, business type systems, and behaviors. This requires concise domain modeling.
2. **Adapters**: The mechanical outside world (e.g., HTTP APIs, databases) with minimal business logic. Code here can be easily generated with little context.
3. **Wiring**: Application composition root.

This skill ensures that the **Domain** is properly modeled, documented, and aligned with a ubiquitous business language before code generation begins.

## The Workflow

When building a new feature, you must strictly follow this workflow. First, determine if the request is a **Domain Feature** (new business logic, capabilities) or an **Adapter Feature** (technical integration, databases, endpoints implementing existing ports).

---

### PATH A: Domain Features

#### 1. The Grilling Phase (Feature Alignment)
- Do NOT jump straight to writing specs. Actively interview the user to establish the feature's requirements.
- **No Technology Allowed**: This phase must be purely business-oriented. Do NOT discuss technical implementation details, architecture, databases, or frameworks. Focus entirely on the business rules, state changes, and value.
- **Core Goal**: Expose implicit assumptions, gaps, blindspots, adversarial concerns, and failure modes.
- If `docs/product.md` does not exist, ask foundational questions to generate it.
- Ensure the feature aligns with the overarching product vision.
- Suggest the user to use the `/grill-me` slash command if they want an interactive interview session.

#### 2. Evolve the Specifications
Once the feature is fully understood and edge cases are resolved, create or update the foundational specs. All of these must be strictly consistent and grounded in the ubiquitous language:
- **`docs/language.md`**: Maintain and evolve the business language. Define canonical Things (nouns), Actions (verbs), and their relationships.
- **`docs/product.md`**: Update this ONLY if the overarching core vision or scope boundaries fundamentally change. Do not touch this for minor features.
- **`docs/feature/domain/<sequence>-<feature-name>.md`**: Document the specific feature's use cases, constraints, and business processes in the canonical language. Use a sequential prefix (e.g., `001-`, `002-`) to track the evolution of features chronologically. *(Note: If the feature is very small or a minor extension, SKIP creating this spec and just update the domain models directly).*

#### 3. Domain Modeling
With the feature defined, create the domain artifacts to navigate code-level decisions:
- **`docs/models/<domain-name>.md`**: 
  - Define the domain type system (only the core, important types).
  - Outline port interfaces (Inbound/Outbound) and the Service orchestration.
  - Detail any business state machines.
  - Ensure everything abides strictly by `docs/language.md`.
- **`docs/mermaid.md`**:
  - Update this system-wide asset ONLY when there is a structural change in domains (e.g., a new domain is introduced or a new cross-domain bridge is formed). Never create per-domain copies of this diagram. Do not touch this for minor internal updates.

---

### PATH B: Adapter Features

#### 1. The Grilling Phase (Technical Alignment)
- Actively interview the user to clarify technical requirements, external systems, protocols, or frameworks being integrated.
- Identify exactly which existing domain ports (from `docs/models/<domain-name>.md`) this adapter will implement (Inbound or Outbound).
- **Strict Rule**: Adapter features MUST NOT change the ubiquitous language (`docs/language.md`) or the core domain models. They merely implement existing interfaces.

#### 2. Document the Adapter Feature
- **`docs/feature/adapters/<sequence>-<feature-name>.md`**: Document the technical integration using a sequential prefix to track history. Specify the ports being implemented, mapping strategies (domain types to/from external types), error translation handling, and any infrastructure constraints. *(Note: If the adapter change is trivial, you may SKIP creating this spec).*

*(Adapter features skip Step 3: Domain Modeling, as the domain must already be defined.)*

---

## Reference Templates

When writing these documents, refer to the adapted templates bundled with this skill in the `templates/` directory. Use your file-reading tools to review them:
- `language.md`
- `product.md`
- `mermaid.md`
- `feature-name.md`
- `domain.md`

They do not have to be followed exactly. Use your judgment to adapt them to this workflow while maintaining their core purpose and adhering to the project's hexagonal architecture guidelines.
