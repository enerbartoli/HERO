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
| A **Level 1** reconciliation or enrichment write | Forecast-partner rows | **Immediate.** No post-processing is needed. |
| A **Level 2.5 (BU-SKU) reconciliation** change broadcast down to Level 1, and shown in the dashboard | Resolved weekly reporting layer | **Saved immediately, distributed on the next scheduled fan-out run for your market.** See the fan-out section below; the run times differ by market. |
| View **resolved dashboard / reporting** | Resolved weekly reporting layer | After the fan-out for your market completes |
| **Publish to Logility** | Resolved HERO state packaged into the export surfaces | **Only through the weekly export pipeline, on the day and time set for your market.** See the export section below. |

## The fan-out (how Level 2.5 changes reach Level 1)

A Level 2.5 adjustment is **saved immediately**, but it does not fan out to forecast partners immediately. HERO post-processing has to distribute the adjustment and rebuild the partner-level surfaces before it shows up at Level 1. **Scheduled processing is the normal path for a Level 2.5 change, not a fallback for something else.**

!!! note "The fan-out: distributes Level 2.5 down to Level 1"
    Each market has its own job, at its own times, Monday to Thursday:

    | Market | Days | Fan-out runs |
    |---|---|---|
    | United Kingdom | Monday to Thursday | 08:00, 11:00 and 14:00 `Europe/London` |
    | Hasbro U.S. | Monday to Thursday | 12:00, 15:00 and 18:00 `America/New_York` |

    Use the row for **your own market**. A United Kingdom user does not have runs at 12:00, 15:00 and 18:00 Eastern, and a United States user does not have runs at 08:00, 11:00 and 14:00 London; the two rows are not interchangeable. Only the United Kingdom and Hasbro U.S. are live with a defined fan-out schedule. For any other market, including Asia Pacific and Latin America, the honest answer is that no fan-out schedule has been defined yet, not a copy of either row above.

**Level 1 writes remain immediate** and need no post-processing; that is the distinction to hold onto. Level 1 lands on save. Level 2.5 lands on the next fan-out run for that market, which by design can be later the same day, not within minutes of saving.

## The weekly export to Logility

This is a **separate process from the fan-out above**, and it runs on a different day, once a week, inside the export pipeline:

| Market | Day | Export pipeline post-processing runs at |
|---|---|---|
| United Kingdom | Friday | 10:15 `America/New_York` |
| Hasbro U.S. | Saturday | 12:00 `America/New_York` |

Do not merge this table with the fan-out table above; they are different jobs, on different days, and mixing them produces a schedule that matches neither.

## The dashboard has its own cadence

The Power BI dashboard is not refreshed by your upload. It is rebuilt on a schedule of its own, after HERO's materialisation step has run.

!!! note "Dashboard refresh"
    The current cadence is **90 minutes**, with a target of one hour maximum. The constraint is hosting: the dashboard runs in an individual session rather than a service context.

    If you have heard "15 minutes" quoted, that figure described something else — the delay between a load and the underlying data being updated, not the dashboard's own refresh cadence.

## What runs on its own, and what still needs a person

!!! tip "HERO does run scheduled jobs"
    Running without anyone triggering it: ingestion of the Resultant baseline on its own scheduled path, the fan-out jobs above, the cycle refresh and post-processing jobs that build each cycle's render snapshots, the previous-cycle computation, dashboard materialisation and the Power BI refresh, and the weekly export pipeline for each market, which runs whether or not anything changed that week.

    Still needing a person: anything changed directly in Logility, because HERO never reads it. Seeing a new cycle, because your workbook is a point-in-time snapshot that has to be re-downloaded. And clearing a stale adjustment, because a display fix corrects what you see, not what you entered.

## Publication to Logility

!!! warning "Logility is updated only through the weekly export"
    Uploading a workbook does **not** push Logility. HERO publishes to Logility **only through the weekly export pipeline for your market** (see the table above: Friday for the United Kingdom, Saturday for Hasbro U.S.). Anything authored during the week is held in HERO until that pipeline runs for your market. (Downstream transport from Databricks into Logility is external orchestration; see [Batch orchestration & updates](../reference/batch-orchestration-updates.md).)

!!! note "What is sent is not what you typed"
    You author a **delta** in HERO (a plus or minus change). What the export sends is a **complete replacement value** for the affected array and week cell, not the delta itself. Those are two different things, and the distinction is behind several questions users ask about what shows up on the other side.

    HERO also **rounds output to whole units** at partner, SKU, and week grain. Where a Level 2.5 adjustment fans out to many partner cells as fractions, each cell is rounded on its own, so small aggregate differences can appear between a BU-SKU total and the sum of its partner rows. That rounding, not a calculation error, is usually the answer to "why doesn't my BU-SKU total tie exactly to the sum of the partners."

## Urgent changes — the three governed paths

!!! warning "The weekly export is not skippable, use one of these three paths instead"
    HERO exports to Logility only through the weekly export for your market, regardless of urgency. If a change cannot wait for that cadence, it must go through one of these three governed paths, depending on what it is:

    1. **Commercial enrichments** (promos, sets, samples, pre-orders, TMOs) **always** go through HERO — even inside the months 0–4 frozen window. Never enter these directly in Logility.
    2. **Time-sensitive enrichment changes** (e.g. a DI-to-DOM flip): capture it in HERO and flag it as time-sensitive. A weekly report surfaces it to Demand Planning, who executes it in Logility within the agreed weekly window.
    3. **Non-forecast-related edits only** (allocation support, ship-match alignment, holding the month, operational visibility): made directly in Logility on UA1, only within months 0–4, by whoever performs this work today — never flowing into consensus. There is no dedicated NFR (Non-Forecast-Related) functionality in HERO v1.0; this is a deliberate, phased choice. See [Deferred in v0](../reference/deferred-in-v0.md).

## Practical rules

!!! tip "Four rules to live by"
    - A workbook download is a **point-in-time** extract of the current state.
    - A successful upload updates HERO **authoring** state immediately. A Level 1 write is done at that point. A Level 2.5 write still needs its market's next fan-out run before it reaches Level 1 or the dashboard.
    - **Re-download** if someone else has touched the same scope, especially before a later-stage reconciliation session.
    - Publication to Logility happens **only through the weekly export pipeline for your market**, not on upload.

## Related pages

- [Batch orchestration & updates](../reference/batch-orchestration-updates.md) — the full export step and downstream orchestration detail.
- [Where HERO fits in the planning flow](../getting-started/hero-in-the-cycle.md)
- [FAQ & common gotchas](../help/faq-common-gotchas.md)

!!! warning "Gaps & Open Questions"
    - **Fan-out schedules for Asia Pacific and Latin America.** `[GAP: Rene Bartoli / Jarred Bultema]` Not yet configured. Until they are, the answer for those markets is that no fan-out schedule is defined, not a copy of the United Kingdom or Hasbro U.S. rows above.
