# 02 · Split the monolith before Q4

- **Model (internal):** few-truths (judgment)
- **Role & stakes:** Senior engineer in a design review. Q4 peak launch is in 6 weeks. A teammate has proposed extracting `billing` out of the core monolith into its own microservice "so deploys stop breaking checkout."
- **Across the table:** Priya, the Engineering Manager, deciding whether to greenlight the 4-week extraction sprint starting Monday.

## Opening brief

> "The team is exhausted from deploy freezes—two of the last three billing deploys broke checkout. Extracting billing into its own service feels like the cleanest fix before Q4. What do you want to look at before we call it?"

- **D1 (Opening):** Proposal: extract `billing` module into `billing-svc` (estimated 4 weeks, 3 engineers) to stop billing changes from breaking checkout.

## Locked facts (reveal on ask)

- **Why the last 3 incidents happened (D2 — key turn):**
```
incident #1  billing migration added NOT NULL to shared `orders`
incident #2  billing changed return type of helper called by checkout
incident #3  unrelated deploy failed CI (flaky billing test)
```
- **Database coupling (D3):** `billing` and `checkout` both read/write the `orders` and `users` tables in the same Postgres instance. Extracting the service *without* splitting the DB means either cross-service DB writes or building a new internal API + dual-write sync.
- **Test & CI setup (D4):** There are no module boundary checks or contract tests between `billing` and `checkout`. All tests run in one 28-minute suite.
- **Team & timeline (D5):** 6 weeks to Q4 freeze. The 3 engineers proposed for extraction are the same 3 who own Q4 checkout promo features (which aren't done yet).
- **Deploy frequency & infra (D6):** Team deploys ~4 times/week. They have no service mesh, no distributed tracing, and no dedicated on-call rotation for a second service.
- **Alternative effort (D7):** Enforcing a modular boundary (lint/import rules + contract tests + separate migration review for `orders`) takes ~3–4 days.

## Hidden tension

The pain is real (coupled deploys), but extracting a microservice in 4 weeks before Q4 swaps a *code coupling* problem for a *distributed systems + shared DB* problem—while starving Q4 features and adding operational overhead. Modular boundaries + migration guards solve 90% of the actual incidents in 4 days.

## Closing prompt

Give Priya a 2–4 line recommendation on whether to extract now, what to do instead, and why.
