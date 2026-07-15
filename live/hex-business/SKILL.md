---
name: hex-business
description: Brainstorm and refine initial business requirements, enforce consistent vocabulary, and narrow scope to produce docs/business.md.
---

# hex-business

## Purpose
Takes raw, initial business requirements and rigorously refines them into a precise, solid, and actionable business document (`docs/business.md`). This process involves fundamental analysis, identifying vulnerabilities, enforcing strict vocabulary consistency, and keeping the human (USER) in the loop to eliminate assumptions. The output of this skill serves as the foundational input for establishing the ubiquitous language (`docs/vocab.md`) and domains in a Hexagonal Architecture project.

## General Approach (Human-in-the-Loop & Purely Business)
- **Purely Business Oriented**: No technical or code-related brainstorming will be done here. Strip away all technical implementation details and focus entirely on the business domain.
- **Consistent Terminology**: Enforce strict vocabulary consistency (as in ubiquitous language) throughout the process. Use one word per concept (no synonyms), avoid homonyms, prefer common industry terms over clever ones, and clearly separate Things (nouns) from Actions (verbs).
- **Human-in-the-Loop**: Do not generate the final document immediately or assume you know what the user wants. Present your analysis at every step in a clear, digestible format.
- **Continuous Clarification**: Across all the consecutive steps below, your primary directive is to ask pointed questions for clarifications. The goal is to establish the business world as clearly as possible to help navigate the downstream coding agents towards the precise intent. Iterate with the USER until the core business boundaries are crisp, precise, and unambiguous. Use the `ask_question` tool if multiple-choice alignment is helpful, or prompt the user directly.

## Instructions

1. **Establish the Business World & Intent (Define and Scope)**:
   - Read the initial business requirements provided by the USER.
   - Define and scope the business: Establish exactly what the ultimate goal looks like.
   - Identify what business processes are present and map out the overarching "business world" this system lives in.
   - Use the `search_web` tool if needed to research industry standards, existing models, or terminology related to this business world.
   - Ensure a completely clear, shared intent is established before moving deeper.

2. **Fundamental Analysis (Boil it Down)**:
   - Deconstruct the business intent down to its absolute fundamentals (first principles).
   - Identify the core problem being solved and the primary value proposition.

3. **Vulnerability & Gap Analysis**:
   - **Gaps & Blindspots**: What is glaringly missing from the initial requirements? (e.g., edge cases, error handling, regulatory constraints, scale, user lifecycle).
   - **Biases & Implicit Assumptions**: What unstated assumptions exist in the requirements? (e.g., "users will always have internet," "data will always be clean," "payment always succeeds").
   - **Adversarial Attack**: How could a bad actor abuse or break this system? What are the worst-case scenarios and fraud vectors?

4. **Establish Canonical Vocabulary**:
   - Explicitly identify the core nouns (Things) and verbs (Actions) that will describe the business.
   - Present a draft of this vocabulary to the USER to ban synonyms and disambiguate overloaded terms early on.

5. **Narrow the Scope**:
   - Ruthlessly distinguish between "Must Have" (Core MVP) and "Nice to Have" features.
   - Suggest specific areas to cut or defer to simplify the initial business scope.

6. **Draft `docs/business.md`**:
   - Only after the USER confirms the refined requirements and the canonical vocabulary across all preceding steps, generate or update the `docs/business.md` file.
   - Structure `docs/business.md` with:
     - **Core Vision & Fundamentals**: The boiled-down, precise intent.
     - **Canonical Vocabulary**: A brief outline of the enforced nouns and verbs.
     - **Scope Boundaries**: Explicitly defined In-Scope and Out-of-Scope boundaries.
     - **Key Business Scenarios**: Focused descriptions of system behavior and primary workflows, written **strictly** using the canonical vocabulary.
     - **Identified Risks & Mitigations**: Addressed assumptions, edge cases, and adversarial concerns.
   - Ensure the document uses precise, non-technical business language suitable for extracting Domain Nouns (Entities/Value Objects) and Verbs (Ports/Services) in the next phase.

## Output Contract
- The final artifact must be saved to `docs/business.md`.
- It must provide a solid, disambiguated, and terminologically consistent foundation before moving on to bounded context mapping.
