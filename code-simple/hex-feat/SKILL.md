---
name: hex-feat
description: Manages product vision and feature specifications for a Hexagonal Architecture project.
---

# Hexagonal Feature Specifier (hex-feat)

This skill focuses strictly on capturing business requirements, aligning them with the product vision, and documenting the exact scope of a feature without touching domain modeling or code.

## The Workflow

When building a new feature:

### 1. The Grilling Phase (Feature Alignment)
- Actively interview the user to establish the feature's requirements.
- **No Technology Allowed**: If this is a Domain Feature, this phase must be purely business-oriented. Do NOT discuss technical implementation details.
- **Core Goal**: Expose implicit assumptions, gaps, blindspots, adversarial concerns, and failure modes.
- If `docs/product.md` does not exist, generate it using foundational questions.

### 2. Document the Feature
Based on the grilling phase, create or update the feature specs in `docs/feature/`:
- **For Domain Features**: Create `docs/feature/domain/<sequence>-<feature-name>.md`.
- **For Adapter Features**: Create `docs/feature/adapters/<sequence>-<feature-name>.md`.

### 3. Update the Product (Conditional)
- **`docs/product.md`**: Update this ONLY if the overarching core vision or scope boundaries fundamentally change. Do not touch this for minor features.

You do not maintain domain models or ubiquitous language. Once complete, refer the user to the `hex-domain` skill to model the domain changes if needed.

## Reference Templates

When writing these documents, refer to the adapted templates bundled with this skill in the `templates/` directory:
- `product.md`
- `feature-name.md`
