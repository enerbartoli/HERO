<!-- docs/workflows/timing-system-sync.md -->

# Timing & system sync

## Who should read this page

All users. Understanding timing is one of the most important parts of using HERO correctly.

## Purpose

Explain why a download, an upload, a dashboard refresh, and a Logility export do **not** all happen at the same time.

## What updates when

| Action / surface | Reads from | When it updates |
|---|---|---|
| Download an **enrichment-only** workbook | Current HERO lookup data for the selected scope | Immediately, at download |
| Download a **standard reconciliation** workbook | HERO snapshots, Logility forecast data, shipment actuals, price context, prior-cycle metrics where available | Immediately, at download |
| Download a **BU-SKU** workbook | Current aggregated BU-SKU reconciliation view | Immediately, at download |
| **Upload** a valid workbook | HERO raw authored state | Immediately after upload succeeds |
| View **resolved dashboard / reporting** | Resolved weekly reporting layer | After the backend refresh / post-processing run |
| **Publish to Logility** | Resolved HERO state packaged into export arrays | On the configured export cadence (delta-only) |

## Practical rules

!!! tip "Four rules to live by"
    - A workbook download is a **point-in-time** extract of the current state.
    - A successful upload updates HERO **authoring** state immediately, but resolved reporting surfaces may still need the backend refresh to complete.
    - **Re-download** if someone else has touched the same scope — especially before a later-stage reconciliation or sign-off session.
    - Uploading a workbook does **not** push Logility. Publication follows the separate export process.

!!! note
    The specific export schedule and review cadence are set by each market's operating model, not by the tool.

## Related pages

- [Where HERO fits in the planning flow](../getting-started/hero-in-the-cycle.md)
- [FAQ & common gotchas](../help/faq-common-gotchas.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
