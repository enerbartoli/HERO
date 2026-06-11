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
| **Upload** a valid workbook | HERO raw authored state | Authoring state is captured **immediately**; the export later emits only the records you changed |
| A **Level 2.5 (BU-SKU) reconciliation** change broadcast down to Level 1, and shown in the dashboard | Resolved weekly reporting layer | After the next **fan-out** run — **not instantly** |
| View **resolved dashboard / reporting** | Resolved weekly reporting layer | After the fan-out run completes |
| **Publish to Logility** | Resolved HERO state packaged into export arrays (delta-only) | **Only in the weekly weekend batch — Friday afternoon** |

## The fan-out (how Level 2.5 changes reach Level 1)

A Level 2.5 adjustment does not drop to Level 1 the instant you save it. A **post-processing ("fan-out") job** picks it up, distributes it down to the Level 1 partner rows, badges it as a "2.5" change, and feeds the dashboard.

!!! note "Fan-out schedule"
    The fan-out runs **three times a day — around 08:00, 12:00, and 16:00 UTC — Tuesday to Thursday**, covering the captain reconciliation window (Tue–Wed) and the Thursday review window. So a Level 2.5 change becomes visible at Level 1 / in the dashboard at the **next** of those runs.

## Publication to Logility

!!! warning "Logility is updated only on the Friday batch"
    Uploading a workbook does **not** push Logility. HERO publishes to Logility **only in the weekly weekend batch on Friday afternoon (EST)** — the export job runs Friday 12:00pm EST and the Logility extract call at 2:30pm EST. Anything authored during the week is held in HERO until that batch runs.

## Practical rules

!!! tip "Four rules to live by"
    - A workbook download is a **point-in-time** extract of the current state.
    - A successful upload updates HERO **authoring** state immediately, but the dashboard and Level 1 view only catch up at the **next fan-out** (Tue–Thu, 3×/day).
    - **Re-download** if someone else has touched the same scope — especially before a later-stage reconciliation session.
    - Publication to Logility happens **only on the Friday batch** — not on upload.

## Related pages

- [Batch orchestration & updates](../reference/batch-orchestration-updates.md) — the full job chain and export detail.
- [Where HERO fits in the planning flow](../getting-started/hero-in-the-cycle.md)
- [FAQ & common gotchas](../help/faq-common-gotchas.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
