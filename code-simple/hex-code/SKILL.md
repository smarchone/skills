---
name: hex-code
description: Implements features in a Golang Hexagonal Architecture project based on uncommitted domain spec changes.
---

# Hexagonal Code Generator (hex-code)

This skill reads the uncommitted changes (git diff) in the domain and feature specifications and writes the corresponding Golang code according to Hexagonal Architecture guidelines.

## The Workflow

### 1. Analyze Uncommitted Changes
- Run terminal commands (e.g., `git diff` or `git status`) to identify what has changed in the specs (e.g., `docs/models/`, `docs/feature/`, `docs/language.md`).
- Read the changed files to fully understand the feature being implemented and the updated domain models.
- Refer to other specs (like `product.md`) if additional context is needed.

### 2. Implement the Code
Write or update the Golang codebase to reflect the specs:
- **Core Domain (`internal/core/<domain>/`)**:
  - `model.go` & `model_test.go`: Rich domain models, invariants, value objects.
  - `ports.go`: Interfaces for inbound/outbound ports.
  - `service.go` & `service_test.go`: Business orchestration logic.
- **Adapters (`internal/adapters/`)**:
  - Implement inbound adapters (e.g., HTTP, events) and outbound adapters (e.g., DBs, third-party APIs) as required by the feature specs.
- **Wiring (`cmd/main.go`)**:
  - Wire the new ports, services, and adapters together.

### 3. Strict Compliance
- Ensure the code strictly adheres to the canonical vocabulary in `docs/language.md`.
- Ensure all business logic remains in `internal/core/` and adapters remain mechanical without business leakage.
