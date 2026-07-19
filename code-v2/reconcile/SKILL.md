---
name: reconcile
user-invocable: true
disable-model-invocation: true
description: 'Close the loop after an implementation session — detect drift between the code and the snapshots (business.md, domain models), sync the snapshots for intentional evolution, fix code for accidental divergence, and record what changed in the feature folder as a seed for self-improving context.'
---

# reconcile

The pipeline flows *downward* (feature → business → domain → code). An implementation session always
makes decisions the snapshots didn't anticipate, so the code and the snapshots drift apart. `reconcile`
runs **after** a session and flows *upward*: it checks what was actually built against the feature's
intent, **syncs the snapshots** (`docs/business.md` + `docs/models/<domain>.md`) so they mirror the code
again, and **writes what changed into the feature folder**.

Nothing is "done" until reconciliation is clean. The snapshots are the semantic layer; a stale snapshot
is worse than none, because it lies about what the code is.

## State vs. history
- `docs/business.md` and `docs/models/<domain>.md` are **snapshots** — the current "what is". Sync them
  to match what was actually built (for legitimate evolution); they carry no change-history in their prose.
- `docs/features/<name>/` is **history** — the record of one change.
  - `feature.md` is the *intent baseline*. Read it to check what shipped, but do **not** rewrite its
    intent or scenarios. You may update its `status:`; never edit the original ask away.
  - `reconcile.md` is this skill's output: what changed in the snapshots, the drift found, and why.

## What counts as drift (and what doesn't)
Reconcile only the **binding surface** — the parts the snapshots actually promise:
- **Ports** (the contract / seams / bridges), **key types** (aggregate + vocabulary-bearing value
  objects), **invariants**, **vocabulary**, and **use cases**.

Do **not** drag the code's **autonomy zone** into the specs: internal/incidental types, private fields,
helper structs, and internal enums are *meant* to differ from the sketch. Pulling them up is over-
specification and defeats the point of "complete ports, key types only".

## Classify every drift
For each mismatch between code and spec, decide with the USER which it is:
1. **Evolved** — the code made a legitimate, better decision. → **Update the spec** to match. If it
   touches vocabulary or a use case, that goes into `business.md` first, then cascades down.
2. **Bug** — the code diverged by accident and violates the spec's intent. → **Fix the code** to match
   the spec. Do not weaken the spec to cover a mistake.
3. **Underspecified** — the spec was simply silent, and the code had to choose. → Pick the canonical
   answer, write it into the spec, **and record it as a process signal** (see below). This is the most
   valuable class: it's where the harness itself was too thin.

## Process
1. Identify the session's scope: which feature(s) and which `internal/core/<domain>/` packages changed.
   Read the feature doc(s) — they are the intent baseline for the rest of this pass.
2. **Code ↔ feature intent:** compare what shipped against the feature's *Scenarios* and *Out of scope*.
   Did every scenario land? Did anything out-of-scope get built anyway? Were the feature's *Introduces*
   / *Proposes changes* actually adjudicated into `business.md`, or silently dropped? List each gap.
3. **Code ↔ domain snapshot:** compare implemented ports, key types, method signatures, and invariants
   against `docs/models/<domain>.md`. Ignore the autonomy zone. List each drift.
4. **Domain snapshot ↔ business.md:** did any new noun/verb enter the code/sketch without being canonical?
   Did any use case's real behaviour change? List each drift.
5. Classify each drift (evolved / bug / underspecified) with the USER.
6. Apply resolutions: sync the *snapshots* to the code (top-down for any vocab change — business.md →
   domain → code), or fix code. Re-run the domain's tests after any code fix. For `feature.md`, update
   `status:` only — do not rewrite its intent.
7. Update `docs/mermaid.md` if ports/bridges changed.
8. Confirm feature `status:` is `implemented` and the business.md feature index matches reality.
9. Append a `reconcile.md` entry to the feature's folder (template below). If the session advanced more
   than one feature, write an entry in each affected feature's folder. Drift with no clear feature owner
   goes in the session's primary feature.

## Drift record (`docs/features/<name>/reconcile.md`, append-only)

```markdown
## <session label>

**Snapshot changes** — what moved in the snapshots to catch up to the code
- `business.md`: <vocab/use-case changes, or "none">
- `docs/models/<domain>.md`: <ports/key types/invariants changed, or "none">

**Drift & resolution**
| Item (code ↔ snapshot/intent) | Class | Resolution |
|---|---|---|
| <what mismatched> | evolved / bug / underspecified | <snapshot synced / code fixed> |

**Cascaded** — <vocab renames or port changes pushed downstream, or "none">

**Process signal (self-improvement seed)**
- <where a snapshot or a skill was silent, ambiguous, or misleading — a candidate improvement to the
  harness itself. Omit if the session surfaced nothing.>
```

## Self-improving context (future)
The **process signal** lines are the seed. Each one is evidence that a template asked for too little, a
principle was ambiguous, or a layer let information through that it should have caught. A future loop
can glob `docs/features/*/reconcile.md` for recurring signals and feed them back into these skills —
tightening the templates where drift keeps appearing. Keep the signals concrete and honest now; don't
build the mining loop yet. Structure is extracted from real, repeated evidence — not predicted.

## Hand-off
When the drift record is written and the snapshots + code agree on the binding surface, the session is
complete.
