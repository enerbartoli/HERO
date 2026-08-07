<!-- docs/reference/batch-orchestration-updates.md -->

# Batch orchestration & updates

## Who should read this page

Anyone tracing how HERO (Hasbro Enrichment & Reconciliation Optimizer) processes changes and publishes to Logility. For the user-facing *"when does my change take effect?"* view, see [Timing & system sync](../workflows/timing-system-sync.md).

## Purpose

Explain the batch jobs behind HERO, the export to Logility, and the contingency path — the system mechanics beneath the timing rules.

!!! note "When changes take effect — in brief"
    A change is captured in HERO authoring state immediately. It reaches Level 1 and the dashboard after the next post-processing / fan-out run, and it reaches Logility only through the weekly Friday export pipeline. The fan-out runs **multiple times per UK workday** (Mon–Thu at 08:00 / 10:00 / 12:00 / 14:00 / 16:00 / 18:00 and Fri at 08:00 / 10:00 / 12:00 `Europe/London`, plus a Mon–Thu late-night catch-up at 23:00 `America/New_York`). The full schedule is in [Timing & system sync](../workflows/timing-system-sync.md).

## The batch jobs (what each one does)

- **Post-processing / fan-out** — takes Level 2.5 changes authored in HERO, fans them out to the Level 1 partner rows, and refreshes the dashboard-facing Level 1 view. As of the **20 July 2026 release**, post-processing was improved for reliability as usage grows, with better **business-unit scoping** and more **runtime visibility** into the runs.
- **Weekly Logility export** — runs as the Friday noon Eastern export pipeline. It materializes the Logility pickup tables and, if the contingency path is used, the 8-file wide CSV set.

!!! warning "Scheduling is by day-of-week only"
    HERO can only run a job "at this time on this day of the week." It does **not** read the 53-week fiscal planning calendar, so batch timing is expressed as weekday schedules, not planning-cycle dates.

## Direction of travel

The flow is one-way, with exactly one exception.

- Everything HERO manages travels **HERO to Logility**. Only the **Resultant** travels **Logility to HERO**.
- HERO **never reads** UA1, UA2–UA6, ADS2, PROMO_LIFT or ADS3. A change made directly in Logility is therefore invisible to HERO: no download and no upload will bring it in, and it exists in HERO only if someone deliberately makes the equivalent change there.
- The Resultant is read-only to HERO. It can only be changed in Logility, by the baseline owner, which protects the statistical proposal from being overwritten by an export.
- Every array except the Resultant is served to the template from **HERO's own database**, not from a live Logility read. A fresh template download brings in the latest Resultant and the latest HERO state, and nothing else from Logility.
- End-to-end latency on that one inbound path (Logility to EDW to Databricks) exceeds 24 hours, so same-day propagation of a baseline change is not a reasonable expectation.
- Divergence between the two systems is **silent**. Nothing errors, nothing is rejected, and nobody is notified when HERO and Logility stop agreeing. HERO has no view that compares itself against Logility, so the gap closes only by correcting the components in the template.

!!! warning "ADS3 is the one array that can be forced directly"
    HERO neither reads nor writes ADS3 — Logility calculates it as RESULTANT_FORECAST + ADS2 + PROMO_LIFT. Forcing ADS3 directly in Logility therefore cannot desynchronise HERO. It is the exception path for cases that must bypass the forecast entirely. The normal route is still through its components in HERO.

## Export to Logility

The export is changed-row-only, not full-table. HERO emits rows only for changed weekly keys, but each emitted row is fully populated. Unchanged rows are omitted; emitted rows are hydrated according to the outbound rules rather than left blank or sparse.

The full source → array mapping (UA1–UA6, ADS2, and PROMO_LIFT, including how TMO maps to UA5) lives in **[Logility array & mart mapping](logility-array-mart-mapping.md)**. The export rules specific to this layer are:

- **What routes an entry is the template, not the author's role.** Level 1 enrichments of type `MARKETING` and `DEMAND_PLANNING`, captured in the enrichment capture template, do not flow to UA1: they influence the consensus path only, positive values contributing to ADS2 and negative values to PROMO_LIFT. Adjustments made in the **forecast reconciliation template** do flow to UA1, whoever makes them — a Level 2.5 base-trend adjustment entered by Demand Planning or Marketing lands in UA1 exactly as one entered by a Brand Captain or a commercial lead.

    !!! note "This replaces the earlier interim framing"
        Earlier versions of this page described the same behaviour as a temporary limitation, with a role-based exclusion waiting on a user-role validation layer. Routing by template is the ratified design, not an interim state. (Ratified by Rene Bartoli, 6 August 2026.)

- **UA1 composition.** UA1 is the adjusted statistical baseline and also the Sales (Fill) Forecast. It carries the baseline, the Level 1 base-trend adjustment, the Level 2.5 base-trend adjustment (after fan-out), version adjustments, channel shift, and the UA1-mapped enrichment types `PHASE_OUT`, `EXCESS_DEPLETION`, `DEMAND_PHASE_SHIFT` and `SUPPLY_SHORTAGE_COMP`. The shorter formula `BASELINE + BASE_TREND + CHANNEL_SHIFT + PHASE_OUT` used in earlier material was the same fact at a lower level of detail.
- **UA1 frozen horizon:** UA1 is authored by HERO in horizon months **5–21** (rolling, counted from the current date, every cycle — not a one-off period after go-live); in months **0–4** the published value carries the current live Logility UA1 / baseline rather than a HERO-authored overwrite. UA2–UA6, ADS2, and PROMO_LIFT are HERO-managed across months **0–21**.
- **What "changed" means for the export.** The export answers only *"did this value change in HERO since the last HERO export?"* It does not compare HERO against Logility. A direct Logility edit is neither detected nor deliberately overwritten, unless HERO also changed that same intersection during the week, in which case HERO overwrites the arrays it authors.
- **Channel moves generate two updates.** Export keys include shipment channel, so DOM and DI are separate export combinations. Moving an enrichment from one channel to another updates both: the original aggregation is reduced and the new one is created. Multiple enrichment rows sharing SKU, customer, channel and week aggregate together.
- **The zero floor lives in Logility.** Logility prevents any Level 1 combination from being published negative, applying the floor on both sides (RESULTANT_FORECAST + ADS2 + PROMO_LIFT, and the UA arrays). Inside HERO the only negative restriction is on UA1; every other array carries a negative straight out. Because the floor sits on the **total**, a negative hidden under positive components never surfaces downstream, so a published zero is not evidence that the inputs are clean.
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

!!! note "Governance after sign-off is audit-based, not lock-based"
    No technical lock prevents changes after executive sign-off. The control is the cycle-change filter — every change is visible against the last ADS3 summarization — with escalation to leadership for anything that looks like re-inflating the forecast after sign-off. This is a deliberate design choice made after user pushback during discovery.

## Related pages

- [Timing & system sync](../workflows/timing-system-sync.md) — the when-does-my-change-take-effect view.
- [Logility array & mart mapping](logility-array-mart-mapping.md) — the full array mapping.
- [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md)

!!! warning "Gaps & Open Questions"
    - **UA1 upper horizon — pending build confirmation.** Months 5–21 is the design of record (Rene Bartoli, 6 August 2026). On 30 July 2026 the built UA1 export window was described as reaching month 12, and confirmation that the build now matches the design is outstanding.
    - **Frozen-window calculation when a cycle opens in the prior month.** A cycle formally opens the month before its name (the July 2026 cycle opened on 22 June 2026). Whether HERO's rolling window can therefore reach into the last month of the frozen period is not confirmed.
    - **UA2–UA6 direct-edit lockdown.** The Logility permission that allows direct edits on UA2–UA6 and PROMO_LIFT can be removed so that every change flows through HERO. Whether it has been applied, or remains a process rule only, is not confirmed. UA1 stays directly editable inside months 0–4 by design.
