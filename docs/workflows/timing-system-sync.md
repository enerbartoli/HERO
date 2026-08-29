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
| A **Level 2.5 (BU-SKU) reconciliation** change broadcast down to Level 1, and shown in the dashboard | Resolved weekly reporting layer | **In minutes**, triggered by the upload itself — the scheduled wrappers below are a safety net, not the mechanism |
| View **resolved dashboard / reporting** | Resolved weekly reporting layer | After the fan-out completes |
| **Publish to Logility** | Resolved HERO state packaged into the export surfaces | **Only through the weekly Friday export pipeline** |

## The fan-out (how Level 2.5 changes reach Level 1)

**The normal case is immediate.** When you upload a reconciliation or enrichment file, HERO triggers the post-processing refresh on the upload itself, and the partner grain reflects your change **in minutes**. This trigger has no schedule of its own; it runs because you uploaded, not because a time slot arrived. A user who has just uploaded does not wait for a slot.

!!! note "Scheduled wrappers are the safety net, not the mechanism"
    Recurring wrappers around post-processing exist as a backstop, in case the immediate trigger is missed:

    | Wrapper | Days | Times | Timezone | Scope |
    |---|---|---|---|---|
    | UK workday | Monday to Thursday | 08:00, 11:00, 14:00 | `Europe/London` | United Kingdom |
    | US workday | Monday to Thursday | 12:00, 15:00, 18:00 | `America/New_York` | Hasbro U.S. |

    There are no Friday runs and no late-night catch-up run. If you have heard a six-run UK day, a Friday schedule, or a 23:00 catch-up described, that description does not match the current schedule; treat this table as the figure to use.

The answer to "when will my Level 2.5 change reach Level 1" is **minutes after upload**, with the scheduled wrappers as a backstop, not "wait for the next slot."

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

!!! note "What is sent is not what you typed"
    You author a **delta** in HERO (a plus or minus change). What the export sends is a **complete replacement value** for the affected array and week cell, not the delta itself. Those are two different things, and the distinction is behind several questions users ask about what shows up on the other side.

    HERO also **rounds output to whole units** at partner, SKU, and week grain. Where a Level 2.5 adjustment fans out to many partner cells as fractions, each cell is rounded on its own, so small aggregate differences can appear between a BU-SKU total and the sum of its partner rows. That rounding, not a calculation error, is usually the answer to "why doesn't my BU-SKU total tie exactly to the sum of the partners."

## Urgent changes — the three governed paths

!!! warning "The weekly export is not skippable — use one of these three paths instead"
    HERO exports to Logility only through the weekly Friday export, regardless of urgency. If a change cannot wait for that cadence, it must go through one of these three governed paths, depending on what it is:

    1. **Commercial enrichments** (promos, sets, samples, pre-orders, TMOs) **always** go through HERO — even inside the months 0–4 frozen window. Never enter these directly in Logility.
    2. **Time-sensitive enrichment changes** (e.g. a DI-to-DOM flip): capture it in HERO and flag it as time-sensitive. A weekly report surfaces it to Demand Planning, who executes it in Logility within the agreed weekly window.
    3. **Non-forecast-related edits only** (allocation support, ship-match alignment, holding the month, operational visibility): made directly in Logility on UA1, only within months 0–4, by whoever performs this work today — never flowing into consensus. There is no dedicated NFR (Non-Forecast-Related) functionality in HERO v1.0; this is a deliberate, phased choice. See [Deferred in v0](../reference/deferred-in-v0.md).

## Practical rules

!!! tip "Four rules to live by"
    - A workbook download is a **point-in-time** extract of the current state.
    - A successful upload updates HERO **authoring** state immediately, and the dashboard and Level 1 view catch up **in minutes**, triggered by the upload itself, not by waiting for a scheduled slot.
    - **Re-download** if someone else has touched the same scope — especially before a later-stage reconciliation session.
    - Publication to Logility happens **only through the Friday export pipeline** — not on upload.

## Related pages

- [Batch orchestration & updates](../reference/batch-orchestration-updates.md) — the full export step and downstream orchestration detail.
- [Where HERO fits in the planning flow](../getting-started/hero-in-the-cycle.md)
- [FAQ & common gotchas](../help/faq-common-gotchas.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
