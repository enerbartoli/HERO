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
No — it tracks the relationship, but you still capture the compensating demand correctly. Tracking-only refers to the forward forecast: nothing moves between SKUs there. The relationship it records is used at **history cleansing**, where it raises the adjusted demand of the item that was unavailable and reduces the same quantity from the substitute. See [How history cleansing works](../workflows/forecast-range-calculation.md#how-history-cleansing-works).

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
It depends on **which template you used**, not on your role. A Level 1 `MARKETING` or `DEMAND_PLANNING` enrichment captured in the enrichment capture template reaches the consensus only and never touches UA1. An adjustment made in the **forecast reconciliation template** does reach UA1, whoever makes it — including a Demand Planner or a Marketing user. Either way, HERO never overwrites UA1 inside the 0–4-month frozen window. (Ratified by Rene Bartoli, 6 August 2026. This replaces the earlier target-design / pilot-interim answer, which described the same behaviour as a temporary limitation waiting on a user-role layer.)

**I changed UA1 directly in Logility. Will HERO pick it up?**
No, and no amount of downloading or uploading will bring it in. HERO does not read UA1 in any window. The only array HERO reads from Logility is the Resultant. If the change needs to exist in HERO, someone has to make the equivalent change there.

**Does a fresh template download pull the latest UA1 from Logility?**
No. Every array in your template except the Resultant is served from HERO's own database. A fresh download gets you the latest Resultant and the latest HERO state, and nothing else from Logility.

**I removed my adjustment, so why is there still a value in Logility?**
Removing an adjustment zeroes the **delta** that adjustment represented, not the array. And the removal only reaches UA1 while the affected weeks are still **outside** the frozen window. Once those weeks are inside it, HERO does not touch UA1 at all, so the Logility number stays where it was. That is expected behaviour, not a failed upload.

**Logility shows zero, so my inputs must be clean. Right?**
No. Logility applies a zero floor at Level 1, so no Level 1 combination is ever published negative. Because the floor sits on the total, a negative hidden under positive components never surfaces there. Check the total preliminary forecast in HERO instead — a clean published number is not evidence that the components behind it are clean.

**My template is a few weeks old. Can I keep using it?**
Download a fresh one. A template carries the scope you selected **at download time**, and an upload is agnostic to what the dropdowns say now. HERO validates the upload against the latest backend state, so a stale template, or one downloaded at an over-broad scope such as ALL BRANDS, can quietly replace someone else's work in the overlapping scope.

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
