# Hexagonal Architecture Guidelines

When working on hexagonal architecture projects, follow these principles:

## 1. Structure
```
ecommerce-app/
├── cmd/
│   └── main.go                  # Application composition root (Wiring layer)
└── internal/
    ├── core/                    # THE CORE domains (Pure business models, services & ports)
    │   ├── cart/                # Cart Context
    │   │   ├── model.go         
    │   │   ├── model_test.go    # Unit tests for domain models and invariants
    │   │   ├── ports.go         
    │   │   ├── service.go
    │   │   └── service_test.go  # Unit tests for domain service orchestration
    │   └── Order/               # Order Context
    │       ├── model.go         
    │       ├── model_test.go    # Unit tests for domain models and invariants
    │       ├── ports.go         
    │       ├── service.go   
    │       └── service_test.go  # Unit tests for domain service orchestration
    └── adapters/                # THE OUTSIDE (Infrastructure implementations only)
        ├── in/                  # Inbound Adapters (Triggers / Entrypoints)
        │   ├── http/            # Web REST endpoints
        │   └── event/           # Async consumer handling (Kafka / RabbitMQ)
        └── out/                 # Outbound Adapters (External system connections)
            ├── db/              # Persistent databases (PostgreSQL / MongoDB)
            ├── event/           # External message dispatchers
            └── thirdparty/      # Logistics, Dispatch, SMS, and Gateway APIs
```
Each bounded context under `core/` owns its `model.go` (datatypes + business logic),
`model_test.go` (model unit tests), `ports.go` (interfaces), `service.go` (orchestration),
and `service_test.go` (service unit tests).

## 2. Development Guidelines (Inside Out Pattern)
- **Develop domain**: More creative (more business oriented).
- **Develop adapter**: This is more mechanical (and more technical). Adapters just implement the ports for core domains.

## 3. Cross-Domain Calls
Bridge (synchronous, caller needs a result):
- **Use when**: Domain A needs a response from Domain B before continuing.
- Domain A defines an outbound port (e.g. interface in `domainA/ports.go`).
- A bridge adapter (in `adapters/`) implements that port and calls Domain B's inbound port (e.g. Service).
- Domain A never imports Domain B — only the adapter knows about both.
- **Flow**: Domain A → Domain A Outbound Port → Bridge Adapter → Domain B Inbound Port (Service) → Domain B.

## 4. Anti-Pattern
- **Anemic domain models**: This happens when domain models are just data holders and logic is pushed to services.
- To avoid this, create rich domain models with abstractions and composition and let services just stitch and orchestrate.

## 5. Documentation
- **`docs/vocab.md`**: The central source of truth for the ubiquitous language. Defines canonical nouns (Things), verbs (Actions), and relationships. This vocabulary must be strictly consistent, as it directly drives domain modelling and code generation.
- **`docs/mermaid.md`**: A single, system-wide asset containing the Mermaid port diagram. It provides an at-a-glance map of every bounded context and how they connect via bridges or event buses. Never create per-domain copies of this diagram.
- **`docs/models/`**: The directory containing hexagonal domain-model sketches for each bounded context (e.g., `docs/models/{{domain}}.md`). These sketches outline datatypes, interfaces, invariants, and cross-domain interactions without implementations.

## 6. Testing
- **Unit Tests per Model (`model_test.go`)**: Create a unit test file companion to `model.go` to test model invariants, domain actions, and pure business logic. These tests must run completely in-memory, without dependencies on external systems or mocks.
- **Unit Tests per Service (`service_test.go`)**: Create a unit test file companion to `service.go` to test service coordination and orchestration logic. Mock the outbound ports (defined in `ports.go`) to isolate service behavior.
