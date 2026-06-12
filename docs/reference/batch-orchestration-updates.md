<!-- docs/reference/batch-orchestration-updates.md -->

# Batch orchestration & updates

## Who should read this page

Anyone tracing how HERO (Hasbro Enrichment & Reconciliation Optimizer) processes changes and publishes to Logility. For the user-facing *"when does my change take effect?"* view, see [Timing & system sync](../workflows/timing-system-sync.md).

## Purpose

Explain the batch jobs behind HERO, the export to Logility, and the contingency path — the system mechanics beneath the timing rules.

!!! note "When changes take effect — in brief"
    A change is captured in HERO authoring state immediately. It reaches Level 1 and the dashboard after the next post-processing / fan-out run, and it reaches Logility only through the weekly Friday export pipeline. Exact cadence is covered in [Timing & system sync](../workflows/timing-system-sync.md). The current operational schedule is day-of-week based in Eastern time: post-processing runs at 8:00am, 12:00pm, and 4:00pm on Wednesday and Thursday; on Friday it runs at 8:00am and again as part of the 12:00pm export pipeline.

## The batch jobs (what each one does)

- **Post-processing / fan-out** — takes Level 2.5 changes authored in HERO, fans them out to the Level 1 partner rows, and refreshes the dashboard-facing Level 1 view.
- **Weekly Logility export** — runs as the Friday noon Eastern export pipeline. It materializes the Logility pickup tables and, if the contingency path is used, the 8-file wide CSV set.

!!! warning "Scheduling is by day-of-week only"
    HERO can only run a job "at this time on this day of the week." It does **not** read the 53-week fiscal planning calendar, so batch timing is expressed as weekday schedules, not planning-cycle dates.

## Export to Logility

The export is changed-row-only, not full-table. HERO emits rows only for changed weekly keys, but each emitted row is fully populated. Unchanged rows are omitted; emitted rows are hydrated according to the outbound rules rather than left blank or sparse.

The full source → array mapping (UA1–UA6, ADS2, and PROMO_LIFT, including how TMO maps to UA5) lives in **[Logility array & mart mapping](logility-array-mart-mapping.md)**. The export rules specific to this layer are:

- **Marketing / Demand-Planning adjustments do not flow to UA1** — they influence the consensus path only: positive values contribute to ADS2 and negative values contribute to PROMO_LIFT.
- **Residual non-marketing enrichments** influence UA1 and also flow to consensus by sign. This includes `PHASE_OUT`, `EXCESS_DEPLETION`, `DEMAND_PHASE_SHIFT`, and `SUPPLY_SHORTAGE_COMP`.
- **UA1 frozen horizon:** UA1 is authored by HERO only in horizon months **5–12**; in months **0–4** the published value carries the current live Logility UA1 / baseline rather than a HERO-authored overwrite. UA2–UA6, ADS2, and PROMO_LIFT are allowed across months 0–12.
- **Output format:** emitted outbound values are fully populated, exported as whole integers, and rounded to the nearest whole unit with halves rounded away from zero.
- **Delta-table granularity:** the processing tables are weekly-grain, append-by-run history tables. Within a run, HERO emits only the final effective outbound row for each changed weekly key; later runs append new rows for the same weekly key.

## Orchestration chain (weekly)

**HERO-owned weekly export step**

- **Job 1 (Hasbro / Databricks)** — Fridays at 12:00pm Eastern; runs the final post-processing step and then materializes the HERO field-forecast and consensus export artifacts.

**Downstream orchestration (external, not HERO jobs)**

After the HERO export completes, downstream Hasbro / Logility transport and extraction steps pick up those artifacts for processing on the Logility side. These are external orchestration steps, not HERO-internal jobs, and any specific timings or run controls for them are owned in the downstream orchestration spec rather than the HERO repo.

!!! note "Manual runs & transport"
    Controlled manual runs via Run Options are available for testing, pilot validation, and fallback operation. The recurring HERO publish cadence itself is the scheduled Friday export pipeline; any downstream pickup from Databricks into Logility should be understood as downstream orchestration rather than a separate HERO authoring rule.

## Contingency CSV (manual fallback)

If direct integration is not ready, HERO can produce a contingency CSV set for manual loading into Logility: **8 files** (UA1–UA6, Positive Enrichments → ADS2, and Negative Enrichments → PROMO_LIFT). Each file is a wide Level 1 file with 3 key columns and ordinal week columns 1–78. A row appears only if that file's measure changed for that Level 1 key, but every included row is fully populated. Clear rules apply: UA1 clears back to the live Logility UA1 / baseline; UA2–UA6, ADS2, and PROMO_LIFT clear to 0.

## How this connects to the end-to-end process

Baseline generated upstream (Logility / Daybreak) → enrichment capture and reconciliation in HERO (with Level 2.5 changes fanned out to Level 1) → dashboard shows the number **before and after** adjustment → executive sign-off → the weekly Friday export publishes the deltas into the Logility arrays / export surfaces.

## Related pages

- [Timing & system sync](../workflows/timing-system-sync.md) — the when-does-my-change-take-effect view.
- [Logility array & mart mapping](logility-array-mart-mapping.md) — the full array mapping.
- [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
