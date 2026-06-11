<!-- docs/reference/batch-orchestration-updates.md -->

# Batch orchestration & updates

## Who should read this page

Anyone tracing how HERO (Hasbro Enrichment & Reconciliation Optimizer) processes changes and publishes to Logility. For the user-facing *"when does my change take effect?"* view, see [Timing & system sync](../workflows/timing-system-sync.md).

## Purpose

Explain the batch jobs behind HERO, the export to Logility, and the contingency path — the system mechanics beneath the timing rules.

!!! note "When changes take effect — in brief"
    A change is captured in HERO's authoring state immediately, but it only reaches Level 1 / the dashboard at the next **fan-out**, and only reaches Logility on the weekly **Friday export**. The full schedule (fan-out 3×/day Tue–Thu UTC; publish Friday EST) lives in [Timing & system sync](../workflows/timing-system-sync.md).

## The batch jobs (what each one does)

- **Post-processing / fan-out** — takes anything authored at Level 2.5, broadcasts it down to the Level 1 partner rows, badges it as a "2.5" change, and feeds the dashboard. (Dashboard differentiation of 2.5 vs Level 1 is a dashboard-layer function, not core HERO diffing.)
- **Daily regional summarization** — a daily roll-up batch in each region.
- **Weekly Logility export** — the only step that publishes HERO's changes to Logility.

!!! warning "Scheduling is by day-of-week only"
    HERO can only run a job "at this time on this day of the week." It does **not** read the 53-week fiscal planning calendar, so batch timing is expressed as weekday schedules, not planning-cycle dates.

## Export to Logility

The export is **delta-only**: HERO sends a record only for the weeks and items it changed, and gives the **full record** for each changed row — it never overwrites unchanged data with zeros.

The full source → array mapping (UA1–UA6, ADS2, PROMO_LIFT, TMO) lives in **[Logility array & mart mapping](logility-array-mart-mapping.md)**. The export rules specific to this layer are:

- **Marketing / Demand-Planning adjustments do not flow to UA1** — they influence the consensus path (ADS2 for positive, PROMO_LIFT for negative) only.
- **Residual non-marketing enrichments → UA1.** Any enrichment that is *not* a reconciliation adjustment, *not* MARKETING or DEMAND_PLANNING, and *not* explicitly mapped to UA2–UA6 (i.e. `PHASE_OUT`, `EXCESS_DEPLETION`, `DEMAND_PHASE_SHIFT`, `SUPPLY_SHORTAGE_COMP`) influences **UA1**; positive contributes to ADS2, negative to PROMO_LIFT. *(Code alignment of these residual types into UA1 is in branch, pending merge to main.)*
- **UA1 frozen horizon:** UA1 is authored by HERO only in horizon months **5–12**; in months **0–4** the published value carries the current live Logility baseline. UA2–UA6, ADS2, and PROMO_LIFT are allowed across months 0–12.
- **Output format:** fully populated (no nulls), **rounded to the nearest whole integer, halves rounding away from zero.**
- **Delta-table granularity:** the export carries the **latest adjustment per item across all periods of the modified array** — not a running history of every adjustment.

## Orchestration chain (weekly)

1. **Job 1 (Hasbro)** — **Fridays at 12:00pm EST**; populates the HERO field-forecast and consensus delta-history tables.
2. **Job 2 (Hasbro)** — **Fridays at 2:30pm EST**, triggered on Job 1 success; sends a REST call to Logility to extract those tables.
3. **Job 3 (Logility)** — triggered by the REST call; extracts the data, updates an internal staging table, and emails a completion confirmation.

A **process-lock checker** prevents a new run from overlapping one still in progress.

!!! note "Databricks → Logility transport"
    **Post-pilot** the transport is **schedule-based** (run on a schedule). **During the pilot** it is **triggered manually via Run Options**.

## Contingency CSV (manual fallback)

If direct integration is not ready, HERO can produce a **contingency CSV** set for manual loading into Logility: **8 files** (UA1–UA6 plus a positive-enrichments file → ADS2 and a negative-enrichments file → PROMO_LIFT), one row per Level 1 key, with 78 week columns and no null cells. A row appears only if that file's measure changed (delta at row level), but every included row is fully populated (full at cell level). Clear rules apply (UA1 clears to the live Logility baseline; UA2–UA6, ADS2, PROMO_LIFT clear to 0).

## How this connects to the end-to-end process

Baseline generated upstream (Logility / Daybreak) → enrichment capture and reconciliation in HERO (Level 2.5 changes fanned out to Level 1) → dashboard shows the number **before and after** adjustment → executive sign-off → the **weekly Friday export** publishes the deltas into the Logility arrays.

## Related pages

- [Timing & system sync](../workflows/timing-system-sync.md) — the when-does-my-change-take-effect view.
- [Logility array & mart mapping](logility-array-mart-mapping.md) — the full array mapping.
- [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
