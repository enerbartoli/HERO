<!-- docs/reference/documentation-governance.md -->

# Documentation governance

## Who should read this page

Anyone maintaining or contributing to this manual.

## Purpose

State how this documentation is sourced, versioned, and kept honest about uncertainty.

## Source of truth

This manual is consolidated from controlled source documents — primarily the **HERO User Manual (v0)** and the **BU-SKU Reconciliation Behavior Explainer**, with practical examples drawn from the **Module 2** enablement material. Do not add HERO functionality that is not supported by those sources.

!!! note "The HERO product repository is canonical for product behaviour"
    Confirmed by Rene Bartoli, 28 August 2026: the HERO product repository is the canonical source for **what the application does** (the export contract, arrays and horizons, workbook and upload behaviour, formulas, stale-template collisions, enrichment identity and status, the preliminary forecast, dashboard-versus-template timing, missing SKUs, and escalation). Where a page in this manual describes tool behaviour that their repository also documents, it should defer to that source rather than restate it, because their material changes with the code and this manual does not update on the same cadence. This manual remains the only source for the material their repository does not cover: the Forecast Calculation Range as a business process, the Management Indicator, proportioning, the enrichment taxonomy as a decision framework, roles, market scope, and the frozen-window policy as a business rule rather than a horizon number.

## Authority tiers

Adopted 28 August 2026, for this manual's own material. Where two documents disagree, use the higher tier and open a correction against the lower one.

| Tier | Meaning |
|---|---|
| 1 | Current canonical |
| 2 | Current specialised |
| 3 | Proposed or in flight, and **not proof of deployment** |
| 4 | Historical |

## Handling uncertainty

!!! warning "Never hide gaps"
    Where a fact, owner, threshold, date, or policy is not fully defined, it is flagged inline as `[DRAFT — confirm with SME]` and surfaced in the page's **Gaps & Open Questions** block. These are review items, not settled decisions.

## Maintenance conventions

- **One page, one topic.** Keep pages scannable; link rather than repeat.
- **Acronyms expand on first use per page**, even if expanded elsewhere.
- **Admonitions** carry notes, tips, warnings, examples, and open questions — keep the same set across pages.
- When the source documents change, update the affected page and clear or revise its Gaps block.

## Editing and contributions

- Content edits should be grounded in the source documents — not authored freehand.
- Structural / build fixes (links, formatting, navigation) are safe to make directly.
- Material that looks missing or contradictory belongs in the page's Gaps block for SME review, not invented.

The **repository is the source of truth** for manual content. Changes arrive as instructions rather than as inbound packaged archives. The process owner's local folder is a **one-way, read-only copy** of the repository — delivered as a generated snapshot (a zip drop produced on each merge to `main`), copied in by hand, never edited in place and never shipped back as a master. This retires the earlier two-way packaged-archive round-trip, which was itself a place where the repository and the local copy could quietly drift apart.

## Revision log

**2026-08-28** — Landed Canonical Facts sections 17 to 20 (facts 94 to 127), catching the manual up after three earlier update passes did not reach the site. Two of the changes correct guidance the manual was giving confidently and had to be fixed first:

1. **The fan-out schedule is corrected.** The manual described a six-run UK weekday cadence plus Friday runs and a late-night catch-up; none of that exists. The actual mechanism is an immediate, upload-triggered refresh reaching Level 1 in minutes, with recurring UK and US wrappers as a safety net rather than the mechanism. Updated `workflows/timing-system-sync.md` and `reference/batch-orchestration-updates.md`.
2. **Level 2.5 visibility in the Level 1 template is corrected.** A Level 1 user is not blind to a Level 2.5 adjustment in their template; the template carries it as a read-only context column, subject only to the same minutes-after-upload timing as everything else post-processing touches. Updated `tools/bu-sku-level-25-mode.md` and `tools/forecast-reconciliation-template.md`.
3. **The Forecast Calculation Range chapter gained the mechanism it was missing**: the range is a continuous period rather than a year bucket, the Management Indicator (`M` preserves an out-of-range value, `H` removes it) decides what survives it, the range constrains the force down but not the roll up (a different mechanism, the Summing program, handles that), and how the range is built differs by market. Updated `workflows/forecast-range-calculation.md`.
4. **A new recapture case.** When forecast is lost during disaggregation because the range ends before the Consensus Forecast does, the fix is a Level 1 recapture, never a Level 2.5 one; recapturing at Level 2.5 spreads the volume across every extended partner instead of reaching the one that lost it. Detection is manual today; no monitor exists for this yet. New Case 4 in `special-considerations/fcr-adjustment-rules.md`.
5. **Fan-out weighting is described as baseline share**, with the addition that earlier enrichments and carried-forward reconciliation changes do not affect those weights. Updated `tools/bu-sku-level-25-mode.md` and `examples/bu-sku-worked-examples.md`.
6. **A fifth UA1-mapped enrichment type, `NON_STATISTICAL_DEMAND`**, joins `PHASE_OUT`, `EXCESS_DEPLETION`, `DEMAND_PHASE_SHIFT` and `SUPPLY_SHORTAGE_COMP`, and the generating rule behind the list is now taught directly. It captures full forecast volume for a portfolio segment a market has agreed not to forecast statistically, and does not retire the Level 1 base-trend route as an alternative. Updated `reference/logility-array-mart-mapping.md` and `tools/enrichment-capture-template.md`; new glossary entry.
7. **TMO's timing framing was checked and found not to be present** in this manual; no correction was needed.
8. **The UA1 horizon and the frozen window step-down.** The design horizon is confirmed at month 21; the current build stops publishing UA1 at month 12, a known gap being raised for correction rather than a design change. Separately, the frozen window inside which HERO withholds UA1 authoring is stepping down cycle by cycle and is retired entirely from the January 2027 cycle, agreed direction in both pilot markets. Updated `help/glossary.md` and `reference/logility-array-mart-mapping.md`.
9. **The frozen-window carry-forward is stated precisely**: it currently carries the live Logility baseline, not the live UA1 array as intended; the gap narrows as the step-down proceeds. Updated `help/glossary.md`.
10. **What HERO actually sends to Logility.** Users author deltas; the export sends complete replacement values, and output is rounded to whole units at partner, SKU and week grain, which is the usual answer to a BU-SKU total not tying exactly to the sum of its partners. Updated `reference/logility-array-mart-mapping.md` and `workflows/timing-system-sync.md`.
11. **New glossary entries**: Management Indicator, `NON_STATISTICAL_DEMAND`, Summing program, and a tightened Forecast Calculation Range entry that separates it explicitly from the portfolio extension.
12. **One consolidated Power BI dashboard** replaces the earlier separate per-market reports; a user sees the market they are authorised for, and regional-team members see every live market in their region. Updated `tools/reference-views-dashboards.md`.
13. **Documentation governance itself.** Recorded the HERO product repository as the canonical source for product behaviour, with this manual deferring to it on tool mechanics and remaining the only source for the business-process material it does not cover; adopted the four-tier authority model above.

Sourced from `HERO_Canonical_Facts_OnePager_v11_2026-08-28`, the two Logility vendor WebHelp transcriptions in `update_kit/`, and the HERO product repository review in `update_kit/Repo_Docs_Review_2026-08-28.txt`.

**2026-08-07** — Confirmed by Rene Bartoli (process owner) on 7 August 2026:

1. **NPI channel fill corrected — supersedes the NPI extension in item 1 of the 2026-07-16 entry below.** The clause claiming the `+SET/−SET` simplification covered the NPI set/baseline case is removed; it over-extended the 16 July simplification to a case it does not cover. When the Daybreak New Product Introduction launch baseline already embeds the channel fill, the case uses a **negative base trend adjustment in F1** plus a **positive `SET` of equal magnitude in F1**, not a `SET` pair. Sourced from `HERO_Canonical_Facts_OnePager_v5_2026-08-07` fact 45 and `HERO_Build_Learnings_KnowledgeBase_for_Brave_v11_2026-08-07` section 24. Updated `tools/enrichment-capture-template.md`.
2. **Authoring levels by role stated explicitly.** Key Account Managers author at Level 1; Brand Captains, Demand Planning and Marketing at Level 2.5; the Resultant is never modified in either case. Clarifies the phrase "Level 2-only overrides, Level 1 resultant untouched" — it means the Level 1 Resultant is not overwritten, not that Level 1 authoring stops. Updated `getting-started/roles-permissions.md`.
3. **New page: which items have a statistical baseline.** States the rule that a market agrees which segments are forecast statistically, and that segments outside it are captured in full as base trend at Level 1. Includes the United Kingdom and United States differences for Direct Import and FAN, and the United States FAN go-live hold. New `getting-started/statistical-baseline-scope.md`.
4. **The repository is now the source of truth for manual content.** The packaged-archive round-trip is retired; changes arrive as instructions and the process owner's local folder is a one-way, read-only copy delivered as a generated snapshot. Recorded under *Editing and contributions*.
5. **History cleansing documented.** New *How history cleansing works* section in `workflows/forecast-range-calculation.md`: cleansing corrects the Adjusted Demand array so the baseline learns real demand, and runs in the opposite direction to the enrichment — cleansed history is actual shipments minus the `SET`, while base trend adjustments are not cleansed. `SUPPLY_SHORTAGE_COMP` raises the unavailable item's adjusted demand and reduces the substitute's at cleansing. Reconciled the "tracking-only" wording in `tools/enrichment-capture-template.md`, `help/faq-common-gotchas.md` and `workflows/field-by-field-reference.md` so it refers to the forward forecast while the recorded relationship drives cleansing (the existing rule is unchanged, only completed). New `Cleansing` glossary entry in `help/glossary.md`. The cleansing logic is published explicitly as a starting point expected to be refined as cycles accumulate. Sourced from `HERO_Canonical_Facts_OnePager` v6 facts 79–81 and `HERO_Build_Learnings_KnowledgeBase_for_Brave` v12 section 25.

**2026-08-06** — Aligned the manual with the HERO/Logility data flow ratified by Rene Bartoli (process owner) on 6 August 2026 during the Module 7 build, sourced from `HERO_Canonical_Facts_OnePager_v4_2026-08-06` and `HERO_Build_Learnings_KnowledgeBase_for_Brave_v10_2026-08-06`:

1. **Routing is by template, not by role — supersedes item 1 of the 2026-07-12 entry below.** The interim / target-design split is retired. Level 1 `MARKETING` and `DEMAND_PLANNING` enrichments captured in the enrichment capture template do not reach UA1; adjustments made in the forecast reconciliation template do, whoever makes them. Updated `reference/batch-orchestration-updates.md`, `reference/logility-array-mart-mapping.md`, `help/faq-common-gotchas.md`.
2. **Direction of travel documented.** The flow is one-way apart from the Resultant: HERO reads only `RESULTANT_FORECAST` and never reads UA1–UA6, ADS2, PROMO_LIFT or ADS3, so a direct Logility edit is invisible to HERO. New section in `reference/batch-orchestration-updates.md`, summary table in `reference/logility-array-mart-mapping.md`, new glossary entry, four new FAQs.
3. **Horizons corrected.** UA1 is authored across months **5–21** (was 5–12). UA2–UA6, ADS2 and PROMO_LIFT are HERO-managed across months **0–21** (was 0–12). Updated `reference/batch-orchestration-updates.md`, `reference/logility-array-mart-mapping.md`, `help/glossary.md`.
4. **UA1 composition stated in full.** Baseline, Level 1 and Level 2.5 base-trend adjustments, version adjustments, channel shift, plus `PHASE_OUT`, `EXCESS_DEPLETION`, `DEMAND_PHASE_SHIFT` and `SUPPLY_SHORTAGE_COMP`. The shorter four-term formula was the same fact at lower detail; the glossary now links to the composition instead of repeating a partial formula. Phase-out nomenclature from item 2 of the 2026-07-12 entry is unchanged.
5. **Zero floor located.** The floor lives in Logility and works at Level 1; inside HERO only UA1 restricts negatives. Added to `reference/batch-orchestration-updates.md`, `reference/logility-array-mart-mapping.md`, `help/glossary.md`, `help/faq-common-gotchas.md`.
6. **TMO clarified.** TMO passes through exactly as stored, lives in UA5, and never sums into ADS3 the way the other arrays do. A TMO change in HERO still updates UA5 through the field-forecast export. Updated `reference/logility-array-mart-mapping.md`.
7. **Export change detection, channel moves and template scope.** The export only answers whether a value changed in HERO since the last export; channel moves update both the DOM and DI combinations; templates are scope-locked at download time. Updated `reference/batch-orchestration-updates.md` and `help/faq-common-gotchas.md`.
8. **Scheduled jobs and dashboard cadence.** HERO does run scheduled jobs; the dashboard refresh cadence is 90 minutes for now, target one hour, and the "15 minutes" figure quoted in a training session referred to something else. New sections in `workflows/timing-system-sync.md`.
9. **Access model.** Platform-managed regional groups, no role granularity, exactly two levels (planner for Level 2.5, regular user for Level 1), and a ticket lead time to plan around. New section in `getting-started/roles-permissions.md`.

**2026-07-16** — *Backfilled on 7 August 2026 from `CLAUDE_CODE_PROMPT_8.md`. The changes below were written into the manual pages on 16 July 2026 — the ratified DEMAND_PHASE_SHIFT-vs-SET decision together with the 20 July 2026 HERO release — but were never recorded in this revision log; this entry restores the record. It documents edits already present in the pages and changes no content.* Sourced from `CLAUDE_CODE_PROMPT_8.md` and the `HERO_Manual_Site_for_code_2026-07-16_v6` site source:

1. **DEMAND_PHASE_SHIFT replaces SET for re-phasing demand — ratified 16 July 2026.** Re-phasing existing demand between weeks (pull-forwards, push-outs, deals) is captured with a `DEMAND_PHASE_SHIFT` **positive + negative pair**, not `SET`. `SET` is reserved for a true set build; a set build that also pulls existing demand forward pairs a positive `SET` with **negative `SET` rows** on the source weeks — the same enrichment type on both legs. A single `DEMAND_PHASE_SHIFT` row still moves nothing on its own. **Boundary rule:** timing changes that do **not** originate in history go through `DEMAND_PHASE_SHIFT`; phasing issues stemming from baseline/history defects or one-offs not adjusted in time go through **reconciliation** (base trend adjustment). **Disambiguation:** the automated offsetting zero-out belongs to **Channel Shift** (`DOM` ↔ `DI`, a reconciliation control), which creates its negative automatically; `DEMAND_PHASE_SHIFT` moves demand between weeks with both legs authored manually. Updated `tools/enrichment-capture-template.md` (types table, tip, boundary note, warning, and Gaps block replacing its success block) and `help/faq-common-gotchas.md`. *(The extension of this `+SET/−SET` simplification to the NPI set/baseline case — where the launch baseline already carries the fill — is superseded by item 1 of the 2026-08-07 entry above; that case uses a negative base trend adjustment plus a positive `SET`, not a `SET` pair.)*
2. **DECLINED now cancels an enrichment — behaviour flip.** Previously Status was a log-only field and the only way to remove an enrichment's effect was to zero the quantity. As of the **20 July 2026 release** a `DECLINED` row is preserved in the template and audit trail but **excluded from calculated downstream outputs**, and setting Status to `DECLINED` is the recommended way to cancel an enrichment (zeroing the quantity still works). Updated `tools/enrichment-capture-template.md` (Status note and *Cancelling or removing an enrichment*), `help/faq-common-gotchas.md` (two Q&As flipped, one now answering "Yes"), and `workflows/field-by-field-reference.md` (Status row).
3. **Upload validation catches blanked headers and mid-sheet blank rows.** As of the 20 July 2026 release these are rejected with an explanation instead of silently dropping the data below them. New "New checks — 20 July 2026 release" section in `help/validation-error-catalogue.md`; blank-row guidance updated in `tools/enrichment-capture-template.md` and `help/faq-common-gotchas.md`.
4. **Duplicate uploads warn instead of block.** Repeated uploads of the same template now raise a warning and allow an intentional override, where they were previously blocked silently. Updated `help/validation-error-catalogue.md` and `help/faq-common-gotchas.md`.
5. **Reconciliation template improvements.** Clearer labels and formatting, rounded display values, visible calculated forecast totals, clearer Level 1 vs Level 2.5 attribution, and removal of stale/invalid planning SKUs. New "What changed in the 20 July 2026 release" section in `tools/forecast-reconciliation-template.md`.
6. **Rounding note broadened to template display.** Reconciliation templates now show rounded display values for readability while the stored values remain unrounded; export rounding (nearest integer, halves away from zero) is unchanged. Updated `examples/calculation-reference.md`.
7. **Access controls by Business Unit.** Users see only the Business Units they are authorised for in the BU selection. Updated `getting-started/roles-permissions.md` and `workflows/field-by-field-reference.md`, with a "partially superseded" note on the permission-matrix bullet in `reference/deferred-in-v0.md`.
8. **Post-processing reliability, BU scoping and runtime visibility.** The post-processing / fan-out step was improved for reliability as usage grows, with better business-unit scoping and more runtime visibility into runs. Updated `reference/batch-orchestration-updates.md`.

**2026-07-12** — Aligned the manual with facts confirmed by Rene Bartoli (process owner) on 12 July 2026, sourced from `HERO_Build_Learnings_KnowledgeBase_for_Brave_v4_2026-07-12` (sections 13–16) and the corrected S&OP Data Architecture v2 / NFR Addendum v2:

1. **UA1 routing — interim vs target design.** *(Superseded by item 1 of the 2026-08-06 entry above — routing is by template, not by role.)* The claim "Marketing / Demand-Planning adjustments do not flow to UA1" is the *target* design. Reframed with a pilot-interim admonition: during the pilots, all Level 2.5 base-trend adjustments flow to UA1 regardless of author, because the user-role validation layer is not yet built. Updated `reference/batch-orchestration-updates.md` and `help/faq-common-gotchas.md`.
2. **Phase-out nomenclature.** Confirmed canonical name **Phase-out** (written as `PHASE_OUT` in the tool/enrichment-type field), the fourth component of the UA1 formula; `MDP_ENRICHMENT` documented as a legacy synonym only, never current terminology. Updated `help/glossary.md` and `reference/logility-array-mart-mapping.md`. *(The four-term formula here is expanded by item 4 of the 2026-08-06 entry above — same fact, fuller detail; the Phase-out nomenclature is unchanged.)*
3. **Frozen window wording.** Confirmed 4 months, rolling (months 0–4 from the current date, every cycle) — not a one-off post-go-live period, and not "0–90 days" (an erratum in the prior NFR Addendum). Added an explicit glossary entry.
4. **Urgent changes — three governed paths.** Documented the three paths for changes that can't wait for the weekly Friday export: commercial enrichments always through HERO; time-sensitive enrichment changes via HERO + weekly report; non-forecast-related edits directly on UA1 in Logility, months 0–4 only. Updated `help/faq-common-gotchas.md`, `workflows/timing-system-sync.md`, and `reference/deferred-in-v0.md`.
5. **NA-training clarifications.** Confirmed and documented: Level 2.5 adjustments persist as deltas until manually reversed; a Level 2.5 correction disaggregates across all customers by baseline proportion and cannot target one account; Version Change / Channel Shift pairs must be manually zeroed once the Forecasting Range is fixed; KAMs have no access to Level 2.5 templates; governance after sign-off is audit-based (cycle-change filter), not lock-based. Updated `roles/demand-planner.md`, `roles/sales.md`, `tools/forecast-reconciliation-template.md`, and `reference/batch-orchestration-updates.md`.

!!! success "No open questions identified"
    No open questions were identified from the available source material.
