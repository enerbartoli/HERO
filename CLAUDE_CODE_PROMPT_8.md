# Prompt 8 for Claude Code — 20 July 2026 HERO release update + DPS-vs-SET decision (clean replace, then rebuild)

I'm sharing the full, current repository as `HERO_Manual_Site_for_code_2026-07-16_v6.zip`.
This is the source of truth for content. Do a clean replace, not a merge.

## v6 note (re-export)
The v5 zip you inspected had 9 truncated .md files — a sync-cache issue on my side, not content loss.
This v6 zip contains the complete files; verify no file ends mid-word before replacing.

## Exception to the clean replace — Phase-out wording
For `help/glossary.md` and `reference/documentation-governance.md` the **repo version wins**: keep the
2026-07-14 corrected phrasing ("Phase-out is the canonical name (PHASE_OUT is that same name as it
appears in the tool)"). The zip's copies of those 2 files predate that fix — do NOT let the zip regress
them. After the rebuild, include the current content of those 2 files in your report so the local master
can be back-synced.

## What to do
1. Unzip and **replace your repo copy entirely** with its contents (docs/, mkdocs.yml, assets,
   instruction files), EXCEPT the 2 files listed above where the repo version wins. Discard older
   versions of any other .md and of mkdocs.yml — the zip wins.
2. **Do not rewrite or invent content.** Markdown/links/formatting/theme fixes only. Preserve every
   `!!! success "No open questions identified"` block AND every new
   `!!! warning "Gaps & Open Questions"` block — some pages now intentionally have open questions again.
3. Build: `pip install mkdocs-material` then `mkdocs build --strict` — expect **0 warnings**
   (26 pages, 0 broken links).
4. Encoding check: `grep -rlP '\x00' docs/ mkdocs.yml` must return nothing.

## What changed since you last synced (20 July 2026 HERO release)
Nine behavior changes shipped in HERO. The content below is already written into the pages — do NOT
alter the facts, only fix rendering issues if any:

- **DECLINED enrichments (the critical flip).** Previously the manual said Status was log-only and
  the only way to cancel an enrichment was zeroing the quantity. **That is now inverted:** `DECLINED`
  rows are preserved in the template/audit trail but **excluded from calculated downstream outputs**,
  and setting Status to `DECLINED` is the **recommended** way to zero out an enrichment. Updated in:
  `tools/enrichment-capture-template.md` (Status note + "Cancelling or removing an enrichment"),
  `help/faq-common-gotchas.md` (two Q&As flipped, one now answers **Yes**),
  `workflows/field-by-field-reference.md` (Status row).
- **Upload validation** now catches blanked headers and mid-sheet blank rows instead of silently
  dropping data — new section "New checks — 20 July 2026 release" in `help/validation-error-catalogue.md`;
  blank-row guidance updated in `tools/enrichment-capture-template.md` and `help/faq-common-gotchas.md`.
- **Duplicate uploads** now warn + allow intentional override (previously silently blocked) —
  note in `help/validation-error-catalogue.md`, new FAQ in `help/faq-common-gotchas.md`.
- **Reconciliation template improvements** (clearer labels, rounded display values, calculated
  forecast totals, clearer Level 1 vs 2.5 attribution, stale/invalid planning SKUs removed) —
  new section "What changed in the 20 July 2026 release" in `tools/forecast-reconciliation-template.md`.
- **Rounding note broadened** (display + export) in `examples/calculation-reference.md`.
- **BU access controls** — users only see authorised Business Units:
  `getting-started/roles-permissions.md`, `workflows/field-by-field-reference.md`, and a
  "partially superseded" note on the permission-matrix bullet in `reference/deferred-in-v0.md`.
- **Post-processing reliability / BU scoping / runtime visibility** noted in
  `reference/batch-orchestration-updates.md`.
- **DEMAND_PHASE_SHIFT replaces SET for re-phasing demand (RATIFIED, 16 July 2026).** Previously
  the manual called `DEMAND_PHASE_SHIFT` a tracking-only badge and pointed week moves to
  reconciliation. Now: re-phasing demand (pull-forward/push-out, deals) is done with a
  `DEMAND_PHASE_SHIFT` **positive + negative pair**; `SET` is reserved for true set builds (a set
  that also pulls demand forward = positive `SET` + **negative `SET` rows** — same type both legs,
  simplification confirmed 16 July 2026). A single `DEMAND_PHASE_SHIFT` row still does not move
  demand. **Boundary rule:** DPS is for timing changes NOT originating from problems in history;
  phasing issues stemming from baseline/history defects or one-offs not adjusted in time (or not
  explained by commercial actions) go through **reconciliation** (base trend adjustment).
  **Disambiguation:** the automated zero-out belongs to **Channel Shift** (DOM↔DI, a reconciliation
  control) — `DEMAND_PHASE_SHIFT` moves demand between weeks with both legs authored manually.
  Updated in: `tools/enrichment-capture-template.md` (types table, tip + boundary note + warning,
  Gaps block replacing its success block) and `help/faq-common-gotchas.md` (DPS Q&A).

## Verified facts (don't alter)
- All previously verified facts from Prompt 7 still hold (fan-out schedule, Friday Logility publish,
  rounding away from zero on export, UA1 composition, delta-table grain).
- The DECLINED behavior change is effective **as of the 20 July 2026 release** — the pages date it
  that way on purpose; do not remove the "as of" framing.
- The DPS decision is dated **16 July 2026 (ratified)** — keep that framing too.

## Report
Confirm `mkdocs build --strict` passes and give the live GitHub Pages URL, plus the current content of
`help/glossary.md` and `reference/documentation-governance.md` for local back-sync.
