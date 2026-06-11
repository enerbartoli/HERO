<!-- docs/reference/batch-orchestration-updates.md -->

# Batch orchestration & updates

## Who should read this page

All users who need to understand **when a change actually takes effect** — and anyone tracing how HERO (Hasbro Enrichment & Reconciliation Optimizer) publishes to Logility.

## Purpose

Explain which actions update quickly, which wait for a batch run, when those batches run, and how the whole chain connects to the end-to-end forecast enrichment process.

## Quick vs batch — what updates when

| Action | When it takes effect |
|---|---|
| Upload a valid workbook | Authoring state is captured right away; the export only emits the records HERO actually changed. |
| A Level 2.5 (BU-SKU) change broadcast down to Level 1 | After the next **post-processing ("fan-out")** run — not instantly. The change is badged "2.5" and appears in the dashboard. |
| Resolved dashboards / reporting | After the post-processing run completes. |
| Publication to Logility | On the **weekly export batch** (see below). |

!!! note "There is no instant commit"
    HERO is not doing live batch diffing. A change you make becomes visible downstream when the next scheduled job runs, not the instant you save.

## The batch jobs

- **Post-processing / fan-out** — runs **twice a day, Tuesday to Friday**. It takes anything authored at Level 2.5 and broadcasts it down to Level 1, badges it, and feeds the dashboard. A final run happens **right before export**.
- **Daily regional summarization** — a daily roll-up batch runs alongside the weekly job in each region.
- **Weekly Logility export** — runs on a weekly schedule (Fridays) and is what publishes HERO's changes to Logility.

!!! note "Review / frozen window"
    During the review window (Thursday through Friday afternoon), the UI **locks Level 1 enrichment** — this is the frozen window for that cycle.

!!! warning "Scheduling is by day-of-week only"
    HERO can only run a job "at this time on this day of the week." It does **not** read the 53-week fiscal planning calendar, so batch timing is expressed as weekday schedules, not planning-cycle dates.

## Export to Logility

The export is **delta-only**: HERO sends a record only for the weeks and items it changed, and gives the **full record** for each changed row — it never overwrites unchanged data with zeros.

**Array mapping:**

| Source in HERO | Logility array |
|---|---|
| Reconciliation (base trend, version change, channel shift) | **UA1** |
| `RETAIL_PROMOTION` | UA2 |
| `SET` | UA3 |
| `SAMPLE` | UA4 |
| `TMO` | UA5 (excluded from consensus) |
| `PRE_ORDER` | UA6 |
| Positive `MARKETING` / `DEMAND_PLANNING` | **ADS2** (consensus) |
| Negative `MARKETING` / `DEMAND_PLANNING` | **PROMO_LIFT** (consensus) |

!!! note "Two rules to know"
    - **Marketing / Demand-Planning adjustments do not flow to UA1.** They influence the consensus path (ADS2 / PROMO_LIFT) only.
    - **UA1 frozen horizon:** UA1 is authored by HERO only in horizon months **5–12**; in months **0–4** it is withheld and the published value carries the current live Logility baseline. UA2–UA6, ADS2, and PROMO_LIFT are allowed across months 0–12.

**Output format:** published outputs are fully populated (no nulls / not sparse) and **rounded to the nearest whole integer, with halves rounding away from zero.**

## Orchestration chain (weekly)

1. **Job 1 (Hasbro)** — weekly, populates the HERO field-forecast and consensus delta-history tables.
2. **Job 2 (Hasbro)** — triggered on Job 1 success; sends a REST call to Logility to extract those tables.
3. **Job 3 (Logility)** — triggered by the REST call; extracts the data, updates an internal staging table, and emails a completion confirmation.

A **process-lock checker** prevents a new run from overlapping one still in progress.

## Contingency CSV (manual fallback)

If direct integration is not ready, HERO can produce a **contingency CSV** set for manual loading into Logility: **8 files** (UA1–UA6 plus a positive-enrichments file → ADS2 and a negative-enrichments file → PROMO_LIFT), one row per Level 1 key, with 78 week columns and no null cells. A row appears only if that file's measure changed (delta at row level), but every included row is fully populated (full at cell level). Clear rules apply (UA1 clears to the live Logility baseline; UA2–UA6, ADS2, PROMO_LIFT clear to 0).

## How this connects to the end-to-end process

Baseline generated upstream (Logility / Daybreak) → enrichment capture and reconciliation in HERO (Level 2.5 changes fanned out to Level 1) → dashboard shows the number **before and after** adjustment → executive sign-off → the **weekly export** publishes the deltas into the Logility arrays.

## Related pages

- [Timing & system sync](../workflows/timing-system-sync.md)
- [Logility array & mart mapping](logility-array-mart-mapping.md)
- [Forecast range calculation](../workflows/forecast-range-calculation.md)

!!! question "Gaps & Open Questions"
    - Confirm the final **Databricks → Logility transport** (schedule- vs trigger-based) once integration is decided.
    - Residual non-marketing enrichment types (`PHASE_OUT`, `EXCESS_DEPLETION`, `DEMAND_PHASE_SHIFT`, `SUPPLY_SHORTAGE_COMP`) are **intended** to route into UA1 but are not yet aligned in the main code.
    - Confirm the **delta-table granularity** (latest adjustment per item vs all adjustments per item).
