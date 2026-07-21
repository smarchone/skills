---
name: hex-drift
description: Analyzes and reports drift between the specification artifacts and the actual Golang codebase.
---

# Hexagonal Drift Reporter (hex-drift)

This skill acts as an auditor. Its purpose is to report any drift between the intended design (specs) and the actual implementation (code) so that they can be synced if needed.

## The Workflow

### 1. Analyze the Current State
- Read the documentation artifacts: `docs/language.md`, `docs/models/`, `docs/mermaid.md`, and `docs/feature/`.
- Scan the actual codebase structure and code (`internal/core/`, `internal/adapters/`, `cmd/`).

### 2. Identify Drift
Look for discrepancies in the following areas:
- **Vocabulary Drift**: Code (structs, methods, variables) that diverges from the canonical nouns and verbs defined in `docs/language.md`.
- **Architectural Drift**: Business logic leaking into `internal/adapters/`, or core domains importing adapters or sibling domains directly instead of using ports/bridges.
- **Model Drift**: Missing state machines, invariants, or domain types in the code that are defined in `docs/models/<domain>.md`, or vice-versa (code doing things not modeled).
- **Port/Adapter Drift**: Adapters in the code that don't match the modeled ports.

### 3. Report Findings
- Generate a clear, prioritized drift report detailing the mismatches.
- Suggest actionable remediation steps to either update the code to match the specs, or update the specs to reflect reality.
