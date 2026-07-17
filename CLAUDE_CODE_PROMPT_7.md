# Prompt 7 for Claude Code — replace repo with the current zip (content final), then rebuild

I'm sharing the full, current repository as `HERO_Manual_Site_for_code_2026-06-11_v2.zip`.
This is the source of truth for content. Do a clean replace, not a merge.

## What to do
1. Unzip and **replace your repo copy entirely** with its contents (docs/, mkdocs.yml, assets,
   instruction files). Discard older versions of any .md and of mkdocs.yml — the zip wins.
2. **Do not rewrite or invent content.** Markdown/links/formatting/theme fixes only. Preserve every
   `!!! success "No open questions identified"` block.
3. Build: `pip install mkdocs-material` then `mkdocs build --strict` — expect **0 warnings**
   (26 pages, 0 broken links).
4. Encoding check: `grep -rlP '\x00' docs/ mkdocs.yml` must return nothing.

## What changed since you last synced
- **All open gaps are now closed** — every page ends with "No open questions identified."
- **New top-level nav section: "Forecast Calculation Range & Disaggregation"** (file
  `docs/workflows/forecast-range-calculation.md`). It is intentionally a top-level item, not under
  Workflows.
- **De-duplication done** — one owner per topic:
  - `workflows/timing-system-sync.md` owns the user-facing "when does my change take effect" table
    and the fan-out / Friday schedule.
  - `reference/batch-orchestration-updates.md` owns system internals (job chain, transport,
    contingency CSV, export rules) and **links** to Timing and to Logility array mapping instead of
    repeating their tables.
  - `reference/logility-array-mart-mapping.md` owns the array mapping table.
- **Verified facts** (don't alter): fan-out runs 3×/day (~08:00/12:00/16:00 **UTC**), Tue–Thu;
  Logility publish only on the **Friday EST** batch (export 12:00pm EST, REST call 2:30pm EST);
  unit spreads round to nearest integer (halves away from zero); residual non-marketing enrichments
  route to UA1; delta table = latest adjustment per item across all periods.

## Then continue
Proceed with the branding/nav work from `CLAUDE_CODE_PROMPT_4.md` (collapsible nav with chevrons +
larger Hasbro-navy section titles, brand logos per section, texture overlays). Brand rules are in
`BRAND_ASSETS.md` inside the zip.

## Report
Confirm `mkdocs build --strict` passes and give the live GitHub Pages URL.
