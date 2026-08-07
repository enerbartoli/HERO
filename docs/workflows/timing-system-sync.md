<!-- docs/workflows/timing-system-sync.md -->

# Timing & system sync

## Who should read this page

All users. Understanding *when a change actually takes effect* is one of the most important parts of using HERO (Hasbro Enrichment & Reconciliation Optimizer) correctly.

## Purpose

Explain why a download, an upload, a dashboard refresh, and a Logility publication do **not** all happen at the same time.

## What updates when

| Action / surface | Reads from | When it takes effect |
|---|---|---|
| Download any workbook (enrichment-only, standard, or BU-SKU) | Current HERO / Logility data for the selected scope | Immediately, at download (a point-in-time extract) |
| **Upload** a valid workbook | HERO raw authored state | Authoring state is captured **immediately**; the export later emits only the rows you changed |
| A **Level 2.5 (BU-SKU) reconciliation** change broadcast down to Level 1, and shown in the dashboard | Resolved weekly reporting layer | After the next **fan-out** run — **not instantly** |
| View **resolved dashboard / reporting** | Resolved weekly reporting layer | After the fan-out run completes |
| **Publish to Logility** | Resolved HERO state packaged into the export surfaces | **Only through the weekly Friday export pipeline** |

## The fan-out (how Level 2.5 changes reach Level 1)

A Level 2.5 adjustment does not drop to Level 1 the instant you save it. A **post-processing ("fan-out") job** picks it up, distributes it down to the Level 1 partner rows, and refreshes the dashboard-facing Level 1 view.

!!! note "Fan-out schedule"
    The fan-out runs on a frequent, day-of-week schedule so Level 2.5 changes reach Level 1 quickly:

    - **Monday–Thursday (UK workday):** 08:00, 10:00, 12:00, 14:00, 16:00 and 18:00 `Europe/London`.
    - **Friday (UK morning):** 08:00, 10:00 and 12:00 `Europe/London`.
    - **Monday–Thursday late-night catch-up:** 23:00 `America/New_York` (≈04:00 `Europe/London` next day) — so UK users start the next workday with any late-uploaded changes already fanned out.

    A Level 2.5 change becomes visible at Level 1 / in the dashboard at the **next** scheduled run.

## The dashboard has its own cadence

The Power BI dashboard is not refreshed by your upload. It is rebuilt on a schedule of its own, after HERO's materialisation step has run.

!!! note "Dashboard refresh"
    The current cadence is **90 minutes**, with a target of one hour maximum. The constraint is hosting: the dashboard runs in an individual session rather than a service context.

    If you have heard "15 minutes" quoted, that figure described something else — the delay between a load and the underlying data being updated, not the dashboard's own refresh cadence.

## What runs on its own, and what still needs a person

!!! tip "HERO does run scheduled jobs"
    Running without anyone triggering it: ingestion of the Resultant baseline on its own scheduled path, the cycle refresh and post-processing jobs that build each cycle's render snapshots, the previous-cycle computation, dashboard materialisation and the Power BI refresh, and the Friday export batch — which runs whether or not anything changed that week.

    Still needing a person: anything changed directly in Logility, because HERO never reads it. Seeing a new cycle, because your workbook is a point-in-time snapshot that has to be re-downloaded. And clearing a stale adjustment, because a display fix corrects what you see, not what you entered.

## Publication to Logility

!!! warning "Logility is updated only through the Friday export"
    Uploading a workbook does **not** push Logility. HERO publishes to Logility **only through the weekly Friday noon Eastern export pipeline**. Anything authored during the week is held in HERO until that pipeline runs. (Downstream transport from Databricks into Logility is external orchestration — see [Batch orchestration & updates](../reference/batch-orchestration-updates.md).)

## Urgent changes — the three governed paths

!!! warning "The weekly export is not skippable — use one of these three paths instead"
    HERO exports to Logility only through the weekly Friday export, regardless of urgency. If a change cannot wait for that cadence, it must go through one of these three governed paths, depending on what it is:

    1. **Commercial enrichments** (promos, sets, samples, pre-orders, TMOs) **always** go through HERO — even inside the months 0–4 frozen window. Never enter these directly in Logility.
    2. **Time-sensitive enrichment changes** (e.g. a DI-to-DOM flip): capture it in HERO and flag it as time-sensitive. A weekly report surfaces it to Demand Planning, who executes it in Logility within the agreed weekly window.
    3. **Non-forecast-related edits only** (allocation support, ship-match alignment, holding the month, operational visibility): made directly in Logility on UA1, only within months 0–4, by whoever performs this work today — never flowing into consensus. There is no dedicated NFR (Non-Forecast-Related) functionality in HERO v1.0; this is a deliberate, phased choice. See [Deferred in v0](../reference/deferred-in-v0.md).

## Practical rules

!!! tip "Four rules to live by"
    - A workbook download is a **point-in-time** extract of the current state.
    - A successful upload updates HERO **authoring** state immediately, but the dashboard and Level 1 view only catch up at the **next fan-out run** (multiple times per UK workday — see the schedule above).
    - **Re-download** if someone else has touched the same scope — especially before a later-stage reconciliation session.
    - Publication to Logility happens **only through the Friday export pipeline** — not on upload.

## Related pages

- [Batch orchestration & updates](../reference/batch-orchestration-updates.md) — the full export step and downstream orchestration detail.
- [Where HERO fits in the planning flow](../getting-started/hero-in-the-cycle.md)
- [FAQ & common gotchas](../help/faq-common-gotchas.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
