<!-- docs/reference/documentation-governance.md -->

# Documentation governance

## Who should read this page

Anyone maintaining or contributing to this manual.

## Purpose

State how this documentation is sourced, versioned, and kept honest about uncertainty.

## Source of truth

This manual is consolidated from controlled source documents — primarily the **HERO User Manual (v0)** and the **BU-SKU Reconciliation Behavior Explainer**, with practical examples drawn from the **Module 2** enablement material. Do not add HERO functionality that is not supported by those sources.

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

## Revision log

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

**2026-07-12** — Aligned the manual with facts confirmed by Rene Bartoli (process owner) on 12 July 2026, sourced from `HERO_Build_Learnings_KnowledgeBase_for_Brave_v4_2026-07-12` (sections 13–16) and the corrected S&OP Data Architecture v2 / NFR Addendum v2:

1. **UA1 routing — interim vs target design.** *(Superseded by item 1 of the 2026-08-06 entry above — routing is by template, not by role.)* The claim "Marketing / Demand-Planning adjustments do not flow to UA1" is the *target* design. Reframed with a pilot-interim admonition: during the pilots, all Level 2.5 base-trend adjustments flow to UA1 regardless of author, because the user-role validation layer is not yet built. Updated `reference/batch-orchestration-updates.md` and `help/faq-common-gotchas.md`.
2. **Phase-out nomenclature.** Confirmed canonical name **Phase-out** (written as `PHASE_OUT` in the tool/enrichment-type field), the fourth component of the UA1 formula; `MDP_ENRICHMENT` documented as a legacy synonym only, never current terminology. Updated `help/glossary.md` and `reference/logility-array-mart-mapping.md`.
3. **Frozen window wording.** Confirmed 4 months, rolling (months 0–4 from the current date, every cycle) — not a one-off post-go-live period, and not "0–90 days" (an erratum in the prior NFR Addendum). Added an explicit glossary entry.
4. **Urgent changes — three governed paths.** Documented the three paths for changes that can't wait for the weekly Friday export: commercial enrichments always through HERO; time-sensitive enrichment changes via HERO + weekly report; non-forecast-related edits directly on UA1 in Logility, months 0–4 only. Updated `help/faq-common-gotchas.md`, `workflows/timing-system-sync.md`, and `reference/deferred-in-v0.md`.
5. **NA-training clarifications.** Confirmed and documented: Level 2.5 adjustments persist as deltas until manually reversed; a Level 2.5 correction disaggregates across all customers by baseline proportion and cannot target one account; Version Change / Channel Shift pairs must be manually zeroed once the Forecasting Range is fixed; KAMs have no access to Level 2.5 templates; governance after sign-off is audit-based (cycle-change filter), not lock-based. Updated `roles/demand-planner.md`, `roles/sales.md`, `tools/forecast-reconciliation-template.md`, and `reference/batch-orchestration-updates.md`.

!!! success "No open questions identified"
    No open questions were identified from the available source material.
