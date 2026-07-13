# HERO Manual Update Spec — 2026-07-12
Source of truth: `HERO_Build_Learnings_KnowledgeBase_for_Brave_v4_2026-07-12.txt` (sections 13–16) and the corrected architecture docs in this kit. Confirmed by Rene Bartoli on 12 July 2026. Where the manual and these files conflict, these files win.

## Change 1 — UA1 routing: interim (pilot) vs target design  [REQUIRED]
The manual states the TARGET design as current behavior. Reality during the pilots: HERO cannot yet distinguish the author's role on Level 2.5 base-trend adjustments, so ALL Level 2.5 BTAs currently flow to UA1 regardless of who made them (DP, Marketing, or commercial). The role-based exclusion (DP/marketing BTAs -> consensus only, never UA1) activates only once the user-role validation layer is implemented.
- `docs/reference/batch-orchestration-updates.md` (~line 30: "Marketing / Demand-Planning adjustments do not flow to UA1"): reframe as target design + add pilot-interim admonition.
- Grep the whole docs/ tree for any other claim that DP/marketing adjustments never reach UA1 (check `docs/roles/demand-planner.md`, `docs/roles/marketing-gpl.md`, `docs/roles/sales.md`, `docs/workflows/timing-system-sync.md`, `docs/help/faq-common-gotchas.md`) and apply the same interim/target framing.
- Add an FAQ entry in `docs/help/faq-common-gotchas.md`: "Does a DP/Marketing adjustment change my sales forecast (UA1)?" -> interim: yes it can; target: no. Use the wording from KB v4 section 14.

## Change 2 — PHASE_OUT nomenclature  [REQUIRED]
Canonical name confirmed by Rene (12 Jul): **PHASE_OUT** — the manual already uses it, keep it everywhere. The S&OP Data Architecture v2 now carries PHASE_OUT as the fourth UA1 component (UA1 = BASELINE + BASE_TREND + CHANNEL_SHIFT + PHASE_OUT); 'MDP_ENRICHMENT' in the Transmission Design Topics V1 is a LEGACY name for this same component — never introduce it as current terminology.
- Add a glossary entry for PHASE_OUT in `docs/help/glossary.md`: captured in the enrichment capture template; maps depletion of available inventory; part of the UA1 formula; flows to consensus by sign (positive -> ADS2, negative -> PROMO_LIFT); legacy synonym in older architecture material: MDP_ENRICHMENT.
- Verify `docs/reference/logility-array-mart-mapping.md` (UA1 row) and `docs/reference/batch-orchestration-updates.md` (~line 31) reflect that PHASE_OUT feeds UA1 and consensus by sign. Keep the related residual enrichments (EXCESS_DEPLETION, DEMAND_PHASE_SHIFT, SUPPLY_SHORTAGE_COMP) as documented.

## Change 3 — Frozen window wording  [VERIFY + MINOR]
Confirmed: the frozen window is 4 months (rolling horizon months 0–4 from current date). The old "0–90 days" figure was an erratum (already corrected in the NFR Addendum v2, included in this kit). The manual already uses months 0–4 — verify no page says 90 days or frames the window as a one-off post-go-live period, and state "4 months, rolling" explicitly in the glossary if absent.

## Change 4 — Urgent changes: the three governed paths  [REQUIRED if absent]
Verify `docs/help/faq-common-gotchas.md` and `docs/workflows/timing-system-sync.md` cover the three paths (KB v4 section 14, "urgent change" FAQ): (1) commercial enrichments ALWAYS through HERO, even inside months 0–4; (2) time-sensitive enrichment changes (e.g. DI-to-DOM flips): capture in HERO + flag time-sensitive -> weekly report -> DP executes in Logility within the weekly window; (3) non-forecast-related edits only (allocation support, ship-match, holding the month, operational visibility): directly in Logility on UA1, months 0–4 only, by the people who do this today; never flow to consensus. No NFR functionality exists in HERO v1.0, deliberately.

## Change 5 — NA-training clarifications  [VERIFY, add if missing]
From KB v4 sections 13–14, ensure the manual states: (a) Level 2.5 adjustments persist across cycles as deltas until manually reversed (NOT single-cycle); (b) a 2.5-level correction disaggregates across ALL customers by baseline proportion — it cannot target one account; (c) Version Change / Channel Shift pairs must be manually zeroed once the Forecasting Range is fixed; (d) KAMs have no access to Level 2.5 templates; (e) governance is audit-based (cycle-change filter), not lock-based.

## Rules
- Never present open design topics as decided; if a fact is not in the kit files, flag it as `<!-- TODO: confirm with Rene -->` instead of inventing.
- Keep MkDocs Material conventions (admonitions, nav untouched).
- Log this revision in `docs/reference/documentation-governance.md`.
- Run `mkdocs build --strict` and fix any breakage you introduced.
