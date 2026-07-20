---
name: feature
description: Capture a new feature as docs/feature/<name>.md — scenarios, rules, edge cases, and any new business terms. Use whenever the user wants to add, scope, or clarify a feature, or just describes new business behaviour ("add a feature", "we also need to support X", "here's what the product should do") — even without mentioning docs. Produces one feature doc; /update-spec models it into the snapshots afterwards.
---

# feature

A feature is the unit of change and the only place business intent is written down first-hand. Everything else in `docs/` is a snapshot modelled from features by `/update-spec`.

Feature files are append-only history. Each new feature is a new file; a feature already written stays as it was. If the business changes, that is a new feature, not an edit to an old one.

## Process

1. **Read for vocabulary.** `docs/language.md` and `docs/product.md` if they exist, plus recent files in `docs/feature/`. You need to know which words are already spoken for. If none of this exists, this is the first feature — proceed, and `/update-spec` will establish those files later.

2. **Write `docs/feature/<feature-name>.md`.** This is your working space: think here, in the file. Format in `references/feature.md`.

3. **Iterate with the user until they confirm it.** Surface the holes you found and the framings you weighed.

Write nothing outside `docs/feature/`. Not `product.md`, not `language.md`, not a domain spec — propagating a half-understood feature means unwinding it from four files instead of one, and that is exactly what the confirmation step exists to prevent.

## Taste

- **Don't take the first framing that works.** The first shape a feature suggests is usually just the user's phrasing rewritten — which is how they happened to say it, not necessarily how the business works. Before settling, model it at least two ways and see what each costs: does one need fewer new terms? does one keep a rule whole instead of splitting it across two areas of the business? does one survive the edge cases without a special case? Say which you picked and what you rejected. This is the cheapest place in the pipeline to change your mind — a framing that reaches the domain specs is already expensive, and one that reaches code is worse.

- **One word per concept — including the words this feature invents.** Existing concepts use `language.md` verbatim: if the user says "hold" and the vocabulary says **lock**, write **lock** and tell them you did. Genuinely new concepts get declared once in the New terms table and then used identically everywhere in the file — no drifting between "**basket**" in one scenario and "cart" in the next. New terms are held to the same standard as established ones because that is what they become once `/update-spec` runs; a term that arrives inconsistent has to be fixed in every file it already reached.

- **Business language only.** No types, no APIs, no storage. Those belong to the domain spec.

- **Bold every canonical term** in scenarios, so vocabulary drift is visible at a glance.

- **Ask when a scenario has a hole** — an unhandled edge, an undefined actor, an outcome with no trigger. One pointed question costs less than a plausible guess that propagates into code.

## Output format

`docs/feature/<feature-name>.md` — see `references/feature.md`.

## Hand-off

Once the user confirms the feature, `/update-spec` updates `product.md`, `language.md`, and the domain specs from it.
