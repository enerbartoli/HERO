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

**2026-07-12** — Aligned the manual with facts confirmed by Rene Bartoli (process owner) on 12 July 2026, sourced from `HERO_Build_Learnings_KnowledgeBase_for_Brave_v4_2026-07-12` (sections 13–16) and the corrected S&OP Data Architecture v2 / NFR Addendum v2:

1. **UA1 routing — interim vs target design.** The claim "Marketing / Demand-Planning adjustments do not flow to UA1" is the *target* design. Reframed with a pilot-interim admonition: during the pilots, all Level 2.5 base-trend adjustments flow to UA1 regardless of author, because the user-role validation layer is not yet built. Updated `reference/batch-orchestration-updates.md` and `help/faq-common-gotchas.md`.
2. **PHASE_OUT nomenclature.** Confirmed canonical name `PHASE_OUT`, the fourth component of the UA1 formula; `MDP_ENRICHMENT` documented as a legacy synonym only, never current terminology. Updated `help/glossary.md` and `reference/logility-array-mart-mapping.md`.
3. **Frozen window wording.** Confirmed 4 months, rolling (months 0–4 from the current date, every cycle) — not a one-off post-go-live period, and not "0–90 days" (an erratum in the prior NFR Addendum). Added an explicit glossary entry.
4. **Urgent changes — three governed paths.** Documented the three paths for changes that can't wait for the weekly Friday export: commercial enrichments always through HERO; time-sensitive enrichment changes via HERO + weekly report; non-forecast-related edits directly on UA1 in Logility, months 0–4 only. Updated `help/faq-common-gotchas.md`, `workflows/timing-system-sync.md`, and `reference/deferred-in-v0.md`.
5. **NA-training clarifications.** Confirmed and documented: Level 2.5 adjustments persist as deltas until manually reversed; a Level 2.5 correction disaggregates across all customers by baseline proportion and cannot target one account; Version Change / Channel Shift pairs must be manually zeroed once the Forecasting Range is fixed; KAMs have no access to Level 2.5 templates; governance after sign-off is audit-based (cycle-change filter), not lock-based. Updated `roles/demand-planner.md`, `roles/sales.md`, `tools/forecast-reconciliation-template.md`, and `reference/batch-orchestration-updates.md`.

!!! success "No open questions identified"
    No open questions were identified from the available source material.
