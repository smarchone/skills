---
name: build-vs-buy
description: Evaluates Build vs. Buy trade-offs for software solutions. Analyzes unit economics, engineering opportunity costs, scale break-even points, and migration architectures.
---

# Build vs. Buy Evaluator 

## Purpose & Scope
This skill guides the evaluation of whether an organization should purchase a managed SaaS solution or build an internal custom system. It balances business priorities (budget, maintenance, time-to-market) with engineering constraints and long-term technical strategy.

---

## Evaluation Workflow

When presented with a build vs. buy evaluation scenario, execute the following 5-phase analysis:

### Phase 1: Operational & Economic Intake
Gather or infer the key operational metrics:
- **Usage Profile:** Expected volume, throughput, and scale of the solution.
- **Integration Breadth:** Number of upstream and downstream systems that need to connect to the solution.
- **Engineering Overhead:** Fully burdened cost of engineering capacity and team size available for development and maintenance.
- **Performance & SLAs:** Requirements for latency, uptime, and operational intervention.

### Phase 2: Unit Economics & Break-Even Modeling
Calculate the cost asymmetry threshold:
1. **Managed SaaS Baseline:** Compute estimated vendor cost based on usage tiers, seats, or volume formulas. Highlight any hidden penalties or lock-in risks.
2. **DIY Infrastructure Run-Rate:** Compute raw compute, storage, and infrastructure primitives for self-hosting.
3. **Engineering Opportunity Cost:** Factor in the minimum operational maintenance tax (e.g., ongoing maintenance, schema drift, API deprecations, security patching).
4. **Break-Even Verdict:** 
   - If `(Managed SaaS Cost - DIY Cloud Compute Cost) < Engineering Maintenance Cost`: **BUY**.
   - If `(Managed SaaS Cost - DIY Cloud Compute Cost) > Engineering Maintenance Cost` (at scale): **BUILD**.

### Phase 3: Architectural Feasibility Check
Evaluate non-financial disqualifiers:
- **Data Sovereignty & Compliance:** Specific deployment requirements (e.g., air-gapped VPC, GDPR, HIPAA, SOC2).
- **Domain Specialization:** Does the solution require deep, proprietary business logic that a vendor cannot easily accommodate?
- **Performance Constraints:** Strict latency, payload, or edge deployment limits that require custom optimization.

### Phase 4: Migration & Decoupling Strategy
Provide a progressive, non-destructive migration roadmap if building or hybridizing:
1. **Decouple the Contract First:** Enforce open interfaces or abstractions so internal systems are never deeply vendor-locked.
2. **Own the Core Data:** Ensure critical business data remains in customer-owned storage.
3. **Decompose by Layer:** Identify which components are easiest to internalize and which carry high operational drag. Advise against building complex, undifferentiated heavy lifting.

### Phase 5: Persona-Specific Delivery

#### Executive / Business Pitch
Focus on:
- **Capital efficiency:** Diverting engineering from revenue-generating features to undifferentiated infrastructure.
- **Time-to-Market:** Speed of deployment and impact on core business goals.
- **Strategic Risk:** Vendor lock-in versus the burden of long-term internal maintenance.

#### Engineering / Architecture Pitch
Focus on:
- **Maintenance tax:** API drift, rate limits, patching, and edge cases.
- **Extensibility:** Flexibility to modify and extend the system versus waiting on vendor roadmaps.
- **System Isolation:** Clean separation of concerns and architectural boundaries.

---

## Output Template Structure

When responding to a user, structure the deliverable using the following sections:

### 1. Executive Summary & Verdict
[1-2 sentences stating the clear recommendation: Buy, Build, or Hybrid]

### 2. Economic & Resource Analysis
- SaaS Pricing Run-Rate vs. Compute Cost:
- Engineering Opportunity Cost (FTE Allocation):
- Break-Even Horizon:

### 3. Technical Trade-Off Matrix
| Dimension | In-House Build | Managed Platform |
| :--- | :--- | :--- |
| Core Functionality | ... | ... |
| Integration & APIs | ... | ... |
| Compliance & Security | ... | ... |
| Ongoing Maintenance Burden | ... | ... |

### 4. Operational Risk Assessment
- Primary failure modes of building in-house for this context.
- Primary failure modes/risks of buying in this context.

### 5. Architectural Recommendation & Migration Path
[Step-by-step phased approach, specifying how to avoid vendor lock-in]