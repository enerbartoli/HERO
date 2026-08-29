# Build notes (2026-08-28 Canonical Facts catch-up, sections 17-20, facts 94-127)

For Rene. Source: `update_kit/CHANGES_SPEC.md`, `update_kit/HERO_Canonical_Facts_OnePager_v11_2026-08-28.txt`, the two Logility vendor transcriptions, and `update_kit/Repo_Docs_Review_2026-08-28.txt`.

## Self-review pass (before this build)

A prior pass had all thirteen changes applied and committed, but had not been checked against the spec sentence by sentence. This pass re-read the full diff against `CHANGES_SPEC.md`, change by change, and against the four hard constraints. It found and fixed two real gaps:

1. **A missing inline TODO for change 8b.** The spec's own text for 8b opens with the same `<!-- TODO: confirm with Rene -->` syntax as change 6, but the earlier pass had only recorded the open item as a `[GAP: Jarred Bultema]` bracket in a Gaps block, not as a literal inline comment. Added the literal comment to `docs/reference/logility-array-mart-mapping.md`, in the UA1 horizon warning box, right where the note says the export window has been extended: `<!-- TODO: confirm with Rene --> When the export window has been extended to month 21, remove this warning and state month 21 plainly.` The `[GAP: Jarred Bultema]` bracket stays alongside it in the same box and in the two Gaps blocks that reference it; the two are not redundant; the inline comment marks the exact sentence that needs removing, the Gaps block is the reader-facing surfaced item.
2. **Stray em dashes and en dashes in prose from the earlier pass**, missed by that pass's own sweep. Found by grepping added lines against the pre-edit content of each file to separate what I actually wrote from pre-existing text I left alone. Fixed in `docs/reference/batch-orchestration-updates.md` (a bold lead-in phrase and a `[GAP — Jarred Bultema]` tag that had not been converted to the `[GAP: ...]` form used everywhere else), `docs/reference/documentation-governance.md` (the new revision-log entry's own date separator), `docs/help/glossary.md` (the Frozen window entry's number ranges, spelled out as "0 to 4" etc. instead of "0–4"), `docs/reference/logility-array-mart-mapping.md` (two "5–21" ranges and one "0–21" range), `docs/special-considerations/fcr-adjustment-rules.md` (the new Case 4 heading, changed from an em-dash title to a colon title so it does not carry a dash, though it now reads slightly differently from the pre-existing Case 1/2/3 headings, which still use em dashes and were left alone), `docs/workflows/forecast-range-calculation.md` and `docs/workflows/timing-system-sync.md` (one Related-pages bullet and one table cell each). `BUILD_NOTES.md` itself also had three "0–4" ranges in its own prose, fixed the same way.

   Left alone deliberately: table cells using a bare `—` as an empty-value placeholder (an existing convention across several tables in this manual, not prose), the `→` routing arrows in `fcr-adjustment-rules.md`'s Guiding Principle bullets (a distinct symbol from a dash, matching the pre-existing bullets in the same list), and every dash inside text that predates this pass and that I did not otherwise touch.

No content changed as a result of this pass, only punctuation. The thirteen changes and their sourcing are unaffected.

## `<!-- TODO: confirm with Rene -->` placed

Two inline TODO comments, one per the changes that carry one (6 and 8b):

- `docs/tools/enrichment-capture-template.md`, in the new `NON_STATISTICAL_DEMAND` tip block (change 6): the literal value as it appears in the template's Enrichment Type field is unconfirmed. `NON_STATISTICAL_DEMAND` follows the naming convention of every other type on that page, but has not been checked against the live template.
- `docs/reference/logility-array-mart-mapping.md`, in the UA1 horizon warning box (change 8b): when the export window has been extended to month 21, this warning should be removed and the page should state month 21 plainly. Added in the self-review pass above; the earlier pass had only a `[GAP: ...]` bracket for this, not the literal comment the spec's own wording implies.

Change 8d's wording (both pilot markets, not extended beyond them) did not carry its own separate TODO in the spec; it is stated as agreed direction in `docs/help/glossary.md`'s Frozen window entry, not flagged as pending.

The two `[GAP: ...]` brackets that shadow the inline TODOs, surfaced in the reader-facing Gaps blocks rather than as HTML comments:

- `[GAP: Jarred Bultema]`: confirmation that the UA1 export window has been extended to month 21. Placed in `docs/reference/logility-array-mart-mapping.md` (twice: the horizon warning box, next to the inline TODO, and the page's Gaps block) and `docs/reference/batch-orchestration-updates.md` (Gaps block).
- `[GAP: Rene Bartoli]`: the literal `NON_STATISTICAL_DEMAND` template value, carried into `docs/reference/logility-array-mart-mapping.md`'s Gaps block as well as the inline TODO in `docs/tools/enrichment-capture-template.md`, since the spec notes it blocks the array-mapping entry specifically.

## Everything else placed as `[GAP: ...]` in a page's Gaps & Open Questions block

Not asked for as inline TODOs, but genuinely open per the kit, so recorded rather than resolved:

- `docs/workflows/forecast-range-calculation.md`: Level 2 out-of-range scenario not yet exercised in the system (test pending); whether the North America range-construction decision travels to Asia Pacific and Latin America; the range-terminology naming convention; whether a corrective Management Indicator pass over 2026 is planned.
- `docs/special-considerations/fcr-adjustment-rules.md`: whether a forecast-lost check joins the input-data monitor when it is deployed; the same corrective-pass question as above (it's relevant on both pages, per the spec's own open-items list).
- `docs/reference/logility-array-mart-mapping.md`: the four unanswered Logility configuration questions from the vendor-documentation evidence pack (default Resultant Forecast indicator, which Sum Option runs, whether Summing Resultant runs after the FCP, whether the Adjusted Demand `M`/`P`/`Z` set is used in history cleansing).

## Spec items I could not source from the kit

None. All thirteen changes had everything they needed inside `update_kit/`. Where the spec itself flagged something as unresolved (the three TODOs, the open-items list at the end of `CHANGES_SPEC.md`), I carried it forward as a gap rather than guessing, per the spec's own instruction not to silently resolve those.

## Pages where I had to resolve something by judgement

1. **The "frozen window" glossary entry (change 8/9).** The existing entry conflated two things that the canonical facts keep separate: the general months-0-to-4 frozen-window concept used elsewhere in the manual (the "Urgent changes" governed paths in `timing-system-sync.md`, the NFR rule in `deferred-in-v0.md`), and the UA1-specific protection schedule that is now stepping down cycle by cycle and disappears entirely by the January 2027 cycle (fact 116: "the frozen period itself does not disappear, what ends is HERO holding UA1 back inside it"). I rewrote the glossary entry to describe the UA1 step-down precisely, per fact 116's own table, and deliberately did **not** touch the "months 0 to 4" figure used elsewhere for the NFR/urgent-change governed paths, since the spec didn't ask for that and I don't have a source telling me those paths' boundary has itself moved. If those pages' 0-to-4 figure needs to track the step-down too, that's a decision for you, not one I should make silently.
2. **Where to put "you author a delta, the export sends a replacement value" (change 10).** The spec names `docs/reference/logility-array-mart-mapping.md` and `docs/workflows/timing-system-sync.md`. `docs/reference/batch-orchestration-updates.md` already carried the closely related rounding fact ("Output format: ... rounded to the nearest whole unit") from an earlier pass, so I extended that existing line there too rather than leaving it stale next to the new fuller statement on the two spec-named pages. All three now say the same thing; none contradicts another.
3. **The `[GAP: ...]` tag format.** The canonical facts source writes these as `[GAP — Name]` with an em dash. The "no em dashes in prose you write" rule applies to authored text, and I judged a tag I'm choosing to embed counts as that, so I standardized on `[GAP: Name]` (colon) everywhere I added one. It reads the same; flag if you'd rather I match the source's em-dash form exactly for grep-ability against the canonical facts file.
4. **Change 5's "sixth case."** The existing page only had five numbered cases (1, 2, 3A, 3B, 3C), so the new one is "Case 4" rather than literally the sixth item, to keep the page's own numbering scheme intact. It sits closest in shape to Case 3C, as the spec asked, and I added a matching row to the decision-summary table and a bullet to the Guiding Principle list so it doesn't read as bolted on.
5. **Change 7 (TMO) and the "blind to it" wording in change 3 both came back with zero grep hits.** Recorded as findings below rather than as something I decided; see the grep report.

## Grep results (change-sourcing pass)

| Search | Purpose | Hits | Fixed |
|---|---|---|---|
| `08:00`, `10:00`, `16:00`, `23:00`, `Europe/London`, `catch-up` | Change 1: find every copy of the wrong fan-out schedule | 2 files carried the wrong schedule (`workflows/timing-system-sync.md`, `reference/batch-orchestration-updates.md`); the `10:00` hits in `special-considerations/data-transmission-contingency.md` are a different, unrelated weekly export table and were left alone | 2 of 2 |
| `blind`, `does not appear`/`never appears`/`not visible`/`cannot see`, `rely on the dashboard`/`check the dashboard`/`dashboard for` | Change 3: find manual text telling a Level 1 user they can't see a Level 2.5 change | **0** | n/a. The wrong claim lived only in Brave's grounding (Canonical Facts fact 101) and in verbal guidance, never in the manual's own page text. Nothing to correct; I added the correct read-only-column content to `tools/bu-sku-level-25-mode.md` and `tools/forecast-reconciliation-template.md` since it was missing, not wrong. |
| `proportional to the resultant`, `proportion to it` | Change 4: find the old "proportional to the resultant" vocabulary | **0** | n/a. The manual already used "baseline share" / "baseline proportion" everywhere (`tools/bu-sku-level-25-mode.md`, `examples/bu-sku-worked-examples.md`, `examples/calculation-reference.md`, `roles/demand-planner.md`, `help/glossary.md`, `workflows/tab-by-tab-walkthrough.md`). What was missing was the "every enrichment type, not only BTAs" statement and the "earlier enrichments/reconciliation don't affect the weights" fact, both now added. |
| `TMO` (all occurrences, filtered for pallet/FAST/UA5 boilerplate) | Change 7: find TMO framed as a timing exception | **0** | n/a. No page frames TMO as a frozen-window or timing exception. Nothing to correct. |
| `UA1 / baseline`, `UA1/baseline` | Change 9: find every ambiguous "carries the live UA1/baseline" phrasing | 3 (glossary.md once, batch-orchestration-updates.md twice: one in the frozen-horizon bullet, one in the contingency-CSV clear rule) | 3 of 3 |
| `Level 2.5`/`L2.5` near `template`, plus a page-by-page check of `demand-planner.md`, `sales.md`, `marketing-gpl.md`, `field-by-field-reference.md`, `tab-by-tab-walkthrough.md`, `calculation-reference.md`, `faq-common-gotchas.md` | Change 3: confirm no other page repeats the "L1 can't see L2.5" claim | **0** | n/a, same finding as the first row above |

## Anti-regression grep (this pass, run against the final `docs/` tree)

| Grep | Expected | Actual |
|---|---|---|
| `08:00`, `10:00`, `14:00`, `16:00`, `18:00`, `23:00` | Zero as an *asserted schedule* | 3 files match the raw strings, all legitimate: the new correct UK/US wrapper tables in `timing-system-sync.md` and `batch-orchestration-updates.md` reuse `08:00`, `14:00`, `18:00` because the corrected times happen to overlap the old wrong ones (`11:00, 15:00` are the ones that changed); `timing-system-sync.md` also names `23:00` once, only to say no such catch-up exists; `special-considerations/data-transmission-contingency.md`'s hits are an unrelated weekly export table untouched by this pass. The literal old six-run pattern (`08:00, 10:00, 12:00, 14:00, 16:00`) and the old Friday pattern (`08:00, 10:00 and 12:00`) do not appear anywhere. |
| `Europe/London` | Only inside the new two-path block, for the UK safety-net wrapper | Confirmed: 2 hits, both in the new UK-wrapper table/sentence in `timing-system-sync.md` and `batch-orchestration-updates.md`. |
| `catch-up`, `multiple times per` | Zero | `multiple times per`: 0. `catch-up`: 2 hits, both explicitly denying it ("no late-night catch-up run", the revision-log entry recording that the old catch-up "does not exist"); zero as an asserted fact. |
| Friday fan-out runs | Zero; the weekly Logility export may legitimately name a day | Zero fan-out claims. Every remaining "Friday" mention is the weekly Logility export pipeline, a different, still-real mechanism. |
| A Level 1 user cannot see a Level 2.5 change, or must use the dashboard for it | Zero | 2 hits, both negations ("is not blind", "not visible... until post-processing has run", the latter describing the surviving timing fact, not the removed visibility claim). Zero assertions of the wrong claim. |
| `PHASE_OUT` | Every list containing it also contains `NON_STATISTICAL_DEMAND` | Confirmed for every current UA1-composition list (`reference/logility-array-mart-mapping.md`, `reference/batch-orchestration-updates.md`, `tools/enrichment-capture-template.md`'s types table). Two `PHASE_OUT` mentions do not carry `NON_STATISTICAL_DEMAND` alongside them and are correctly left as is: the 2026-08-07 and 2026-07-12 entries in `documentation-governance.md`'s revision log, which record what was true on those dates, before the type existed, and the Phase-out glossary entry, which cross-references the full composition list rather than repeating it. |
| `NON_STATISTICAL_DEMAND` | Present in the array mapping, the enrichment capture template page, and the glossary | Present in all three, plus `batch-orchestration-updates.md` and `documentation-governance.md`. |
| `Management Indicator` | Present in the glossary and in `workflows/forecast-range-calculation.md` | Present in both, plus `special-considerations/fcr-adjustment-rules.md` and `documentation-governance.md`. |
| `"No open questions were identified"` on `special-considerations/fcr-adjustment-rules.md` | Zero | 0. Change 5 replaced it with a real Gaps & Open Questions block. |

## `mkdocs build --strict`

Passes clean, no warnings.

## Consolidated manual

Regenerated with `tools/generate_manual_full.py` (174,832 bytes, 29 nav pages) after the self-review fixes above. `--check` was not re-run after generating since generating *is* the check; the file now matches `docs/` by construction.

## No PR #24 content reverted

`git diff main...HEAD -- docs/index.md mkdocs.yml` is empty; `docs/tools/reference-views-dashboards.md` carries only the new consolidated-dashboard note, and the Power BI link added by PR #24 (`1d7dcc05-0d12-40f8-bd0c-184b82bdd406`) is unchanged in `docs/index.md`, `docs/tools/reference-views-dashboards.md`, `mkdocs.yml`, and the regenerated consolidated manual.

## Drop

Produced with `tools/make_drop.py` after committing, so the manifest's source commit matches the content. `--dest` is the Windows OneDrive path hard-coded as this tool's default for Rene's machine; this session can't write there, so the zip was handed back as a file instead of copied to that folder. Rene (or whoever runs this locally) still needs to do the manual copy the tool describes.

## Nav

Unchanged. No change in this pass needed a new page.
