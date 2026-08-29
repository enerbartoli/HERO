# Build notes (2026-08-28 Canonical Facts catch-up, sections 17-20, facts 94-127)

For Rene. Source: `update_kit/CHANGES_SPEC.md`, `update_kit/HERO_Canonical_Facts_OnePager_v11_2026-08-28.txt`, the two Logility vendor transcriptions, and `update_kit/Repo_Docs_Review_2026-08-28.txt`.

## `<!-- TODO: confirm with Rene -->` placed

Only one inline TODO comment, exactly where the spec asked for it (change 6):

- `docs/tools/enrichment-capture-template.md`, in the new `NON_STATISTICAL_DEMAND` tip block: the literal value as it appears in the template's Enrichment Type field is unconfirmed. `NON_STATISTICAL_DEMAND` follows the naming convention of every other type on that page, but has not been checked against the live template.

The other two TODOs the spec called out (change 8b: when the UA1 export window is confirmed extended to month 21, remove the build-gap note; change 8d wording) I handled as `[GAP: ...]` items in the relevant page's own Gaps & Open Questions block instead of inline HTML comments, because they are not literal-string placeholders sitting inside a sentence; they're standing open questions, which is what those blocks are for. They are:

- `[GAP: Jarred Bultema]`: confirmation that the UA1 export window has been extended to month 21. Placed in `docs/reference/logility-array-mart-mapping.md` (twice: the horizon warning box and the Gaps block) and `docs/reference/batch-orchestration-updates.md` (Gaps block).
- `[GAP: Rene Bartoli]`: the literal `NON_STATISTICAL_DEMAND` template value, also carried into `docs/reference/logility-array-mart-mapping.md`'s Gaps block since it blocks that page's own array-mapping entry, per the spec's own note that this blocks a manual edit there.

## Everything else placed as `[GAP: ...]` in a page's Gaps & Open Questions block

Not asked for as inline TODOs, but genuinely open per the kit, so recorded rather than resolved:

- `docs/workflows/forecast-range-calculation.md`: Level 2 out-of-range scenario not yet exercised in the system (test pending); whether the North America range-construction decision travels to Asia Pacific and Latin America; the range-terminology naming convention; whether a corrective Management Indicator pass over 2026 is planned.
- `docs/special-considerations/fcr-adjustment-rules.md`: whether a forecast-lost check joins the input-data monitor when it is deployed; the same corrective-pass question as above (it's relevant on both pages, per the spec's own open-items list).
- `docs/reference/logility-array-mart-mapping.md`: the four unanswered Logility configuration questions from the vendor-documentation evidence pack (default Resultant Forecast indicator, which Sum Option runs, whether Summing Resultant runs after the FCP, whether the Adjusted Demand `M`/`P`/`Z` set is used in history cleansing).

## Spec items I could not source from the kit

None. All thirteen changes had everything they needed inside `update_kit/`. Where the spec itself flagged something as unresolved (the three TODOs, the open-items list at the end of `CHANGES_SPEC.md`), I carried it forward as a gap rather than guessing, per the spec's own instruction not to silently resolve those.

## Pages where I had to resolve something by judgement

1. **The "frozen window" glossary entry (change 8/9).** The existing entry conflated two things that the canonical facts keep separate: the general months-0–4 frozen-window concept used elsewhere in the manual (the "Urgent changes" governed paths in `timing-system-sync.md`, the NFR rule in `deferred-in-v0.md`), and the UA1-specific protection schedule that is now stepping down cycle by cycle and disappears entirely by the January 2027 cycle (fact 116: "the frozen period itself does not disappear, what ends is HERO holding UA1 back inside it"). I rewrote the glossary entry to describe the UA1 step-down precisely, per fact 116's own table, and deliberately did **not** touch the "months 0–4" figure used elsewhere for the NFR/urgent-change governed paths, since the spec didn't ask for that and I don't have a source telling me those paths' boundary has itself moved. If those pages' 0–4 figure needs to track the step-down too, that's a decision for you, not one I should make silently.
2. **Where to put "you author a delta, the export sends a replacement value" (change 10).** The spec names `docs/reference/logility-array-mart-mapping.md` and `docs/workflows/timing-system-sync.md`. `docs/reference/batch-orchestration-updates.md` already carried the closely related rounding fact ("Output format: ... rounded to the nearest whole unit") from an earlier pass, so I extended that existing line there too rather than leaving it stale next to the new fuller statement on the two spec-named pages. All three now say the same thing; none contradicts another.
3. **The `[GAP: ...]` tag format.** The canonical facts source writes these as `[GAP — Name]` with an em dash. The "no em dashes in prose you write" rule applies to authored text, and I judged a tag I'm choosing to embed counts as that, so I standardized on `[GAP: Name]` (colon) everywhere I added one. It reads the same; flag if you'd rather I match the source's em-dash form exactly for grep-ability against the canonical facts file.
4. **Change 5's "sixth case."** The existing page only had five numbered cases (1, 2, 3A, 3B, 3C), so the new one is "Case 4" rather than literally the sixth item, to keep the page's own numbering scheme intact. It sits closest in shape to Case 3C, as the spec asked, and I added a matching row to the decision-summary table and a bullet to the Guiding Principle list so it doesn't read as bolted on.
5. **Change 7 (TMO) and the "blind to it" wording in change 3 both came back with zero grep hits.** Recorded as findings below rather than as something I decided; see the grep report.

## Grep results

| Search | Purpose | Hits | Fixed |
|---|---|---|---|
| `08:00`, `10:00`, `16:00`, `23:00`, `Europe/London`, `catch-up` | Change 1: find every copy of the wrong fan-out schedule | 2 files carried the wrong schedule (`workflows/timing-system-sync.md`, `reference/batch-orchestration-updates.md`); the `10:00` hits in `special-considerations/data-transmission-contingency.md` are a different, unrelated weekly export table and were left alone | 2 of 2 |
| `blind`, `does not appear`/`never appears`/`not visible`/`cannot see`, `rely on the dashboard`/`check the dashboard`/`dashboard for` | Change 3: find manual text telling a Level 1 user they can't see a Level 2.5 change | **0** | n/a. The wrong claim lived only in Brave's grounding (Canonical Facts fact 101) and in verbal guidance, never in the manual's own page text. Nothing to correct; I added the correct read-only-column content to `tools/bu-sku-level-25-mode.md` and `tools/forecast-reconciliation-template.md` since it was missing, not wrong. |
| `proportional to the resultant`, `proportion to it` | Change 4: find the old "proportional to the resultant" vocabulary | **0** | n/a. The manual already used "baseline share" / "baseline proportion" everywhere (`tools/bu-sku-level-25-mode.md`, `examples/bu-sku-worked-examples.md`, `examples/calculation-reference.md`, `roles/demand-planner.md`, `help/glossary.md`, `workflows/tab-by-tab-walkthrough.md`). What was missing was the "every enrichment type, not only BTAs" statement and the "earlier enrichments/reconciliation don't affect the weights" fact, both now added. |
| `TMO` (all occurrences, filtered for pallet/FAST/UA5 boilerplate) | Change 7: find TMO framed as a timing exception | **0** | n/a. No page frames TMO as a frozen-window or timing exception. Nothing to correct. |
| `UA1 / baseline`, `UA1/baseline` | Change 9: find every ambiguous "carries the live UA1/baseline" phrasing | 3 (glossary.md once, batch-orchestration-updates.md twice: one in the frozen-horizon bullet, one in the contingency-CSV clear rule) | 3 of 3 |
| `Level 2.5`/`L2.5` near `template`, plus a page-by-page check of `demand-planner.md`, `sales.md`, `marketing-gpl.md`, `field-by-field-reference.md`, `tab-by-tab-walkthrough.md`, `calculation-reference.md`, `faq-common-gotchas.md` | Change 3: confirm no other page repeats the "L1 can't see L2.5" claim | **0** | n/a, same finding as the first row above |

## `mkdocs build --strict`

Passes clean, no warnings.

## Consolidated manual

Regenerated with `tools/generate_manual_full.py` (174,656 bytes, 29 nav pages) after all thirteen changes landed. `--check` was not re-run after generating since generating *is* the check; the file now matches `docs/` by construction.

## Drop

Produced with `tools/make_drop.py` after committing, so the manifest's source commit matches the content. `--dest` is the Windows OneDrive path hard-coded as this tool's default for Rene's machine; this session can't write there, so the zip was handed back as a file instead of copied to that folder. Rene (or whoever runs this locally) still needs to do the manual copy the tool describes.

## Nav

Unchanged. No change in this pass needed a new page.
