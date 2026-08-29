# Update kit — 2026-08-28

What is in this kit, and how much authority each file carries. Read this before `CHANGES_SPEC.md`.

## The work order

| File | What it is |
|---|---|
| `CHANGES_SPEC.md` | **The work order.** Thirteen changes, each naming the pages it touches. Execute in order; change 1 first. |

## Source of truth

| File | Authority |
|---|---|
| `HERO_Canonical_Facts_OnePager_v11_2026-08-28.txt` | **Highest.** Ratified by Rene Bartoli. Where the manual and this file disagree, this file wins. The spec lands its sections 17 to 20, facts 94 to 127. Facts are cited by number from the knowledge checks, so never renumber or restate one loosely. |

## Evidence behind the spec

Read these when the spec points you at them. They are why the facts say what they say.

| File | What it is | How to use it |
|---|---|---|
| `Logility_DO_Forecast_Override_Indicators_v1.txt` | Logility vendor documentation, transcribed. The `M` / `H` indicator behaviour and the Summing program. | The mechanism behind change 2b and 2c. Quote the vendor sparingly; the manual is for planners, not for engineers. |
| `Logility_DO_Forecast_Calculation_Range_Logic_v2.txt` | Logility vendor documentation, transcribed. What the Forecast Calculation Range does. | Background for change 2. Neither vendor file is complete without the other. |
| `Repo_Docs_Review_2026-08-28.txt` | The review that produced changes 1 and 2. | Read it if a change is unclear. It explains what was found and why it matters, with the sources named. |

## Not ours, and not to be copied

| File | What it is |
|---|---|
| `HERO_BRAVE_Knowledge_Base_repo.txt` | The HERO product team's own controlled knowledge pack, generated from their repository and stamped against a commit. |

**Do not copy content from this file into the manual.** It is authoritative for product behaviour and it changes with the code. Anything the manual copies out of it becomes a stale second version the moment they ship. Cross-reference it instead.

It covers, and the manual should defer to it on: the export contract, arrays and horizons, workbook and upload behaviour, stale and overlapping template collisions, Excel formula handling, enrichment identity and the `DECLINED` status, the preliminary forecast, dashboard versus template timing, missing SKUs, and the escalation checklist.

It does **not** cover, and the manual remains the only source for: the Forecast Calculation Range as a business process, the Management Indicator, proportioning, the enrichment taxonomy as a decision framework, roles, market scope, and the frozen-period policy as a business rule rather than a horizon number.

## Two things to know about the sources

**The snapshot is behind the running code.** The product documentation this review was based on is commit `1f8017ba`; the repository is at release 2.26.0. The fan-out schedule in change 1 came from the live repository, not from the snapshot. Where the two could differ, the spec carries the live figure.

**Nothing in this kit is a commitment.** Horizons, dates and the protection step-down are directional. Change 8 in particular carries a divergence between design and build that is deliberately recorded as both, and a decision that is approved in one market and pending in another. Do not flatten either into a single clean statement.
