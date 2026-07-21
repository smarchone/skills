---
name: feature
description: Captures a new feature's scenarios, rules, and vocabulary in docs/feature/<name>.md.
---

# feature

A feature is the unit of change and the first-hand record of business intent.
Feature files are append-only. Business changes require new feature files, not edits to old ones.

## Process

1. **Read vocabulary:** Review `docs/language.md` and `docs/product.md`.
2. **Write feature file:** Draft `docs/feature/<feature-name>.md` (see `references/feature.md`). 
3. **Iterate & Confirm:** Discuss with the user until confirmed.

**CRITICAL:** Write nothing outside `docs/feature/`. Do not update `product.md`, `language.md`, or domain specs — that happens during the `/update-spec` hand-off.

## Guidelines

- **Explore framings:** Don't blindly accept the first framing. Model the feature multiple ways. Choose the approach that introduces fewer terms, avoids splitting rules, and handles edge cases cleanly. Explain your choice.
- **Strict vocabulary:** One word per concept. Use existing `language.md` terms exactly as defined. Define new terms once and use them consistently. 
- **Business language only:** No types, APIs, or implementation details.
- **Bold canonical terms** in scenarios to make vocabulary drift obvious.
- **Identify holes:** Ask questions if there are unhandled edge cases, undefined actors, or outcomes without triggers. Do not guess.

## Output Format & Hand-off

- **Format:** `docs/feature/<feature-name>.md` (refer to `references/feature.md`).
- **Hand-off:** Once the feature is confirmed by the user, `/update-spec` updates `product.md`, `language.md`, and the domain specs.
