# Hexagonal build pipeline

Take a business idea to domain code in three reviewable steps.

```
/feature   →   /update-spec   →   /apply
 describe       model into        generate
 the ask        snapshots         the code
```

You describe a feature in plain business terms. It gets modelled into the
snapshots — the product, the language, and the domains. The code follows from
those. Each step waits for your approval before the next one runs.

## Using it

### 1. Describe the feature

> *"customers should be able to cancel an order up until it ships, but not
> after"*

`/feature` writes `docs/feature/cancel-order.md`. It contains the scenarios, the
rules, the edge cases, and any new business terms.

It will ask about gaps it finds. *What happens to a partially shipped order?* It
also shows you other ways it considered framing the feature.

Nothing else is written until you're happy with this file.

### 2. Model it into the snapshots

`/update-spec` folds the feature into three snapshots of the business as it now
stands:

- `docs/product.md` — what the product does and where its scope ends
- `docs/language.md` — the canonical business vocabulary
- `docs/domain/*.md` — one spec per bounded context

The edits are left uncommitted. Review them with `git diff`. Your comments come
back as revisions.

### 3. Generate the code

`/apply` reads the approved specs and writes `internal/<domain>/` — the
aggregate and its invariants, the ports, the service that orchestrates them,
and a test for every business rule.

If existing code contradicts a spec, it stops and asks.

You can also run `/update-spec` on its own — to refresh the docs after they drift, or
to rebuild them from every feature at once.