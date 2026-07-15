---
name: hex-tdd
description: Guide incremental Test-Driven Development (TDD) from the inside out for Hexagonal Architecture, strictly adhering to AGENTS.md.
disable-model-invocation: true
---

# hex-tdd

## Purpose
Drive the implementation of a Hexagonal Architecture Bounded Context using an incremental Test-Driven Development (TDD) cycle. This skill enforces the "Inside-Out" pattern defined in `AGENTS.md`—starting with the pure Domain Core (models and services) using unit tests and mocks, and then moving outward to the Infrastructure Adapters using integration tests.

## Principles (Inside-Out Incremental TDD)
- **Core First (Inside-Out)**: Always develop the `internal/core/<domain>` layer first. The core has zero external dependencies and only imports standard libraries or other core domain models (if bridged).
- **Behavioral Testing**: Tests should read like the business requirements (from `docs/vocab.md` and `docs/business.md`). Test the business *behavior*, not the technical implementation.
- **Interface-First Ports**: Define outbound dependencies as interfaces (`ports.go`) directly in the domain layer *as you discover the need for them* while writing domain tests.
- **Incremental Red-Green-Refactor**: Write one failing test (Red), write the minimal code to pass it (Green), clean up the code (Refactor). Do not write all tests at once; build incrementally.
- **Mocks vs Real Infrastructure**: Use mocks *only* when testing the Domain Core to simulate ports. When testing Adapters, avoid mocking if possible; use real, containerized, or local test infrastructure to ensure the adapter actually works.

## Instructions

### 1. Preparation
- **Read Context**: Familiarize yourself with the target domain by reading `docs/models/<domain>.md` and `docs/vocab.md`.
- **Target Identification**: Pick one focused business scenario or feature to implement.

### 2. Phase 1: Domain Core TDD (Unit Testing)
- **Write a Failing Test**: Create `internal/core/<domain>/model_test.go` or `service_test.go`. Write a test for a single business rule. 
- **Implement Minimal Logic**: Write the minimal code in `model.go` or `service.go` to make the test pass.
- **Define Ports on Demand**: If your service needs to fetch or save data, define that need as an interface in `internal/core/<domain>/ports.go`. Use a mock implementation of this port in your test.
- **Refactor**: Clean up the code.
- **Loop**: Repeat this Red-Green-Refactor cycle until the entire domain behavior for the target scenario is implemented and covered by fast unit tests.

### 3. Phase 2: Outbound Adapters TDD (Integration Testing)
- **Target Outbound Adapter**: Move to `internal/adapters/out/<type>/` (e.g., `out/db` or `out/thirdparty`).
- **Write Integration Test**: Write a test for the adapter implementation. This test should use a real or test-specific environment (e.g., a test database container).
- **Implement Adapter**: Write the adapter code that strictly satisfies the outbound port interface defined in the core domain.

### 4. Phase 3: Inbound Adapters TDD (Handler/Controller Testing)
- **Target Inbound Adapter**: Move to `internal/adapters/in/<type>/` (e.g., `in/http`).
- **Write Request/Response Test**: Write a test using tools like `httptest` (for Go). The test should simulate an incoming request and assert the expected response. You can mock the core domain service here since the core is already tested.
- **Implement Handler**: Write the HTTP handler or event consumer to parse the input, call the domain service, and format the output.

### 5. Phase 4: Composition Root (Wiring)
- **Wire it up**: Once the core and adapters are built and tested, compose them in `cmd/main.go`. Inject the outbound adapters into the domain service, and inject the domain service into the inbound adapters.

## Output Contract
- Code must strictly follow the directory structure in `AGENTS.md`.
- Code must have high test coverage, driven by tests written *before* the implementation.
- The Core Domain must remain pure and free of infrastructure leakage.
