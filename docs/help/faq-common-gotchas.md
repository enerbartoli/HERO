<!-- docs/help/faq-common-gotchas.md -->

# FAQ & common gotchas

## Who should read this page

All users. Quick answers to the questions that come up most often.

## Purpose

Resolve the recurring points of confusion in HERO (Hasbro Enrichment & Reconciliation Optimizer).

## Frequently asked questions

**Why does the dashboard not match my upload yet?**
Your upload updates HERO authoring state immediately, but resolved reporting surfaces update only after the backend refresh completes.

**When should I re-download a workbook?**
Before any major working session, after a validation failure, after another user touched overlapping scope, and when the process moves into BU-SKU review.

**Can I use both Enrichments and Reconciliation?**
Yes, for different jobs: Enrichments for dated business events; Reconciliation for direct week-level number changes after those events are considered.

**Can I upload both standard and BU-SKU reconciliation from the same workbook?**
No. BU-SKU mode is a different authoring mode and is treated separately.

**What does blank vs 0 mean in BU-SKU mode?**
Blank keeps the current rendered BU-SKU adjustment total; `0` sets it to zero for that week; a negative value means the adjustment total should be below zero.

**Does DEMAND_PHASE_SHIFT automatically move demand between weeks?**
Not with a single row. To re-phase demand, author a **positive + negative pair**: a positive `DEMAND_PHASE_SHIFT` row where the demand should land, and a negative row where it is taken from. As of the **16 July 2026 decision (ratified)**, this pair — not `SET` — is the recommended way to re-phase demand; reserve `SET` for true set builds. Use it for deals, pull-forwards and timing changes that do **not** come from problems in history; if the phasing issue stems from baseline/history defects or one-offs not adjusted in time, correct it via **reconciliation** (base trend adjustment) instead.

**Does SUPPLY_SHORTAGE_COMP automatically move volume between SKUs?**
No — it tracks the relationship, but you still capture the compensating demand correctly.

**Can I change actualized weeks?**
Treat shaded / actualized weeks as frozen forecast history unless your operating model explicitly routes an exception through a separate process.

**In the Level 2.5 template, which columns do Demand Planners use for their adjustments?**
The **Baseline Trend Adjustments** columns — the **orange** ones. That is the editable weekly area.

**Then why does my adjustment show under "Marketing and Demand Planning" after I upload?**
Because HERO **classifies** your entry on upload based on **who entered it and when**. You always type into *Baseline Trend Adjustments*; the system then files Demand Planning / Marketing reconciliation entries under the *Marketing and Demand Planning* columns. Both are correct — input vs. how it's classified afterward.

**How do I cancel or delete an enrichment I captured?**
**Never delete the row.** As of the **20 July 2026 release**, set the row's **Status** to `DECLINED` — the row is preserved in the template and audit trail for visibility, but excluded from calculated downstream outputs. Zeroing the quantity still removes the effect, but `DECLINED` is now the recommended method.

**If I set the Status to "Declined", does that cancel the enrichment?**
**Yes — as of the 20 July 2026 release.** A `DECLINED` enrichment is preserved for visibility in the template and audit trail, but **excluded from calculated downstream outputs**. Setting Status to `DECLINED` is now the best way to "zero out" a previous enrichment. (Before this release, Status was log-only and zeroing the quantity was the only method.)

**Can I use formulas (e.g. VLOOKUP) or copy data from other files into the template?**
Yes — the templates are normal Excel files, so use whatever helps while you prepare. Just, **before uploading**: replace formulas with their values (paste as values), don't overwrite rows, avoid blank rows, and add any new/copied rows below the last row with data. As of the **20 July 2026 release**, upload validation catches blanked headers and mid-sheet blank rows and rejects the upload instead of silently dropping data — see [Validation & error catalogue](validation-error-catalogue.md).

**What happens if I upload the same template twice?**
As of the **20 July 2026 release**, HERO warns you that the upload looks like a duplicate and lets you **intentionally override** where appropriate, instead of silently blocking the repeat upload. Best practice is unchanged: **download a fresh template before every working session** and avoid stale saved templates. If you see any template/dashboard mismatch, report it immediately.

**Does a DP/Marketing adjustment change my sales forecast (UA1)?**
It depends on the phase. **Target design:** no — Demand Planning / Marketing adjustments flow only into consensus, never into UA1 (the field/sales forecast). **Pilot interim (current):** HERO does not yet have the user-role layer needed to tell who authored a Level 2.5 base-trend adjustment, so for now **all** Level 2.5 base-trend adjustments flow into UA1 regardless of who made them. True in both phases: Marketing Enrichment and Demand Adjustment components never migrate to UA1, and HERO never overwrites UA1 inside the 0–4-month frozen window. (Confirmed by Rene Bartoli, 12 July 2026.)

**I made an urgent change and Logility doesn't show it yet — is HERO broken?**
No. HERO exports to Logility only once a week (Friday), by design — see [Timing & system sync](../workflows/timing-system-sync.md). If a change genuinely cannot wait, there are three governed paths, depending on what it is:

1. **Commercial enrichments** (promos, sets, samples, pre-orders, TMOs) **always** go through HERO — even inside the months 0–4 frozen window. Never enter these directly in Logility.
2. **Time-sensitive enrichment changes** (e.g. a DI-to-DOM flip): capture it in HERO and flag it as time-sensitive. A weekly report surfaces it to Demand Planning, who executes it in Logility within the agreed weekly window.
3. **Non-forecast-related edits only** (allocation support, ship-match alignment, holding the month, operational visibility): made directly in Logility on UA1, only within months 0–4, by whoever performs this work today. These never flow into consensus. There is no dedicated NFR (Non-Forecast-Related) functionality in HERO v1.0 — this is a deliberate, phased choice.

## Related pages

- [Timing & system sync](../workflows/timing-system-sync.md)
- [Validation & error catalogue](validation-error-catalogue.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
