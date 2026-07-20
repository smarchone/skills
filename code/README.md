# Hexagonal build pipeline

Take a business idea to domain code in three reviewable steps.

```
/feature   →   /update-spec   →   /domain
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

`/domain` reads the approved specs and writes `internal/<domain>/` — the
aggregate and its invariants, the ports, the service that orchestrates them,
and a test for every business rule.

If existing code contradicts a spec, it stops and asks.

You can also run `/update-spec` on its own — to refresh the docs after they drift, or
to rebuild them from every feature at once.

## Features and snapshots

Two kinds of document, doing opposite jobs.

**Features are the log.**
One file per feature. Written once, never revised. If the business changes,
write a new feature. All the history lives here.

**Snapshots are the current state.**
Product, language, and domains. Rewritten in place, every time. They never
accumulate history — they describe the business as it is today. That's what the
features are for.

If you've seen an event log with a projection built off it, this is that shape.

### What each snapshot is for

**Product and language are the mental model.**
These aren't docs *about* the system. They're the context you need to change it.
What the business is doing, and the exact words it uses. Read them before
touching domain code. They're what stops an agent inventing a synonym or naming
a type after the wrong idea.

**Domain specs are the control surface.**
This is where you steer the code, while steering is still cheap. Move a rule to
another context. Rename a port. Add an invariant. The code follows.

At the spec you're reviewing a decision. Once it's Go, you're reviewing an
implementation.

## Why it works this way

**Features are the only source.** The snapshots are modelled from them, never
edited independently. A new feature can rewrite what an old one established.
That's correct, not a conflict — a snapshot is the business now, not a pile of
amendments.

**One word per concept.** The same term appears in the product doc, the spec,
and the Go type. No synonyms. So you can grep a business word and land on the
code — with no index to maintain.

This is also why `/update-spec` resists adding terms. One synonym breaks that,
everywhere, quietly.

**Every rule names its error.** Each business rule pairs with the `Err…` value
it returns. You can trace a line of code back to the rule behind it. And the
tests write themselves: one case per rule.

**The diff is the proposal.** Skills write changes and leave them uncommitted.
Review with `git diff`. Approve by committing. Nothing to keep in sync.

**Every step stops for review.** A bad framing caught at `/feature` costs one
file. Caught at `/domain`, it costs a rewrite.

## Limits

**New bounded contexts are proposed, not created.** `/update-spec` explains why it
thinks one is needed. You decide.

**`/domain` writes the core only.** No adapters, no wiring. The spec lists what
`cmd/main.go` needs so you can wire it yourself.

**The pipeline runs one way.** Edit code directly and the specs won't know. The
next `/domain` run catches the mismatch and stops for you to resolve — but until
then the spec describes something that isn't there. Prefer changing the spec and
re-running `/domain`.
