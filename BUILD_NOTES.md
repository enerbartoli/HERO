# Build notes (2026-08-29 fan-out correction, Canonical Facts section 21, facts 128-130)

For Rene. This pass re-reads `update_kit/CHANGES_SPEC.md` as corrected on 2026-08-29 (fourteen changes now, source of truth `HERO_Canonical_Facts_OnePager_v15_2026-08-29.txt`, sections 17 to 21, facts 94 to 130).

## What this pass actually is

Changes 2 through 13 were unchanged between the previous kit and this one (confirmed by a byte diff of both `CHANGES_SPEC.md` versions). They were already applied and self-reviewed in the prior pass, merged as PR #25, and needed no rework. Only two things changed: change 1 was rewritten because the version applied yesterday was itself wrong, and a new change 14 was added. This pass redoes change 1 correctly and applies change 14.

## Why change 1 had to be redone

Yesterday's fix read a `jobs.run_now` upload trigger in the product repository and concluded a Level 2.5 change fans out to Level 1 in minutes, with the scheduled runs as a safety net behind it. That is wrong. Per the corrected fact 118 (Jarred Bultema, who authors the product documentation): a Level 2.5 change is saved immediately but is **not** distributed immediately; HERO post-processing has to run, and scheduled processing is the **normal path** for that, not a fallback. Worse, yesterday's fix also merged two genuinely different processes, the fan-out (Monday to Thursday, per market) and the weekly export post-processing (once a week, on a different day per market), into a single table. Both errors are now corrected.

## What changed, by page

- `docs/workflows/timing-system-sync.md`: the "What updates when" table now has a separate Level 1 row (immediate); the Level 2.5 row says "saved immediately, distributed on the next scheduled fan-out run for your market" with no minutes promise. "The fan-out" section states the two-process distinction in prose, then carries only the fan-out table (UK Mon-Thu 08:00/11:00/14:00 Europe/London, US Mon-Thu 12:00/15:00/18:00 America/New_York). A new "The weekly export to Logility" section carries the separate export table (UK Friday 10:15, US Saturday 12:00, both America/New_York), explicitly telling the reader not to merge the two tables. The dashboard-cadence, "urgent changes", and "practical rules" sections had their Friday-only and minutes wording corrected to be per-market and process-correct. Replaced "No open questions identified" with a Gaps block carrying the one open item from section 21: Asia Pacific and Latin America schedules are not yet configured.
- `docs/reference/batch-orchestration-updates.md`: the "in brief" note, the two batch-job bullets, the weekly export orchestration-chain bullet (previously a single "Fridays at 12:00pm Eastern" line, now two per-market lines matching the corrected schedule), the manual-runs note, and the end-to-end arrow chain all corrected the same way.
- `docs/help/faq-common-gotchas.md`: "HERO exports to Logility only once a week (Friday)" corrected to state both markets' days.
- `docs/tools/bu-sku-level-25-mode.md` and `docs/tools/forecast-reconciliation-template.md`: both had a leftover "minutes after upload" promise for Level 2.5 visibility at Level 1 from yesterday's fix, missed by yesterday's own self-review because the wrong figure was consistent across every page it touched at the time. Both now say "the next scheduled fan-out run for that market."
- `docs/reference/documentation-governance.md`: annotated the 2026-08-28 revision-log entry's items 1 and 2 to record that the fix they describe was itself wrong for one day, without rewriting the historical entry itself. Added a new 2026-08-29 entry with the real fix and the change-14 market-bloc-scope note the spec asks for.

## Change 14

Grepped `docs/` for "North America, Asia Pacific and Latin America", "non-FAST markets", "non-FAST bloc", and every `FAST` occurrence. Result: the manual never actually states a market-bloc-implies-shared-schedule claim. The only `FAST` mentions are strictly about TMO capture and sourcing (`roles/sales.md`, `tools/enrichment-capture-template.md`, `help/glossary.md`), which fact 128 explicitly says is the legitimate scope of that grouping. The "North America" / "Asia Pacific and Latin America" mentions are all in `workflows/forecast-range-calculation.md`, about how the Forecast Calculation Range is built, a business/process rule (fact 99), correctly carrying a `[GAP: ...]` about whether it travels rather than asserting that it does. Nothing needed correcting in page bodies; the short note the spec asks for is in `documentation-governance.md`'s new revision-log entry above.

## `<!-- TODO: confirm with Rene -->` still in place

Both from the prior pass, untouched by this one:

- `docs/tools/enrichment-capture-template.md`: the literal `NON_STATISTICAL_DEMAND` template value (change 6).
- `docs/reference/logility-array-mart-mapping.md`: the UA1 export-window extension to month 21 (change 8b).

No new TODOs were needed this pass; nothing in change 1 or 14 was left open pending Rene, since fact 118 and facts 128 to 130 gave complete, specific figures for the two live markets and a clear "not yet defined" for the others.

## Spec items not sourceable from the kit

None.

## Judgement calls

1. **Extending the fix beyond the lines the spec quoted verbatim.** Change 1's "what the manual says today, wrong, remove it" list quotes only the schedule block in `timing-system-sync.md` and the admonition in `batch-orchestration-updates.md`. But both pages also carried older, pre-existing statements describing the weekly export as a single "Friday noon Eastern" job (the orchestration-chain "Job 1" bullet, the "Publication to Logility" warning, the FAQ answer). Leaving those as they were would have put a corrected two-market export table next to unmodified prose asserting a single Friday time, an on-page contradiction. I corrected all of them to the same two-market figures fact 118 gives, since it is the same underlying process, not a new one.
2. **What to do with yesterday's revision-log entry.** Rather than rewriting it, which would erase the record that a wrong fix was briefly live, I followed this file's own established convention (see the 2026-08-07 entry's parenthetical notes on the 2026-07-16 and 2026-07-12 entries) and added parentheticals to items 1 and 2 pointing at today's correction, then logged the real fix as its own dated entry.
3. **The Gaps block added to `timing-system-sync.md`.** Not explicitly requested by change 1 or 14, but fact 129's own "Open items on this section" names exactly this gap (Asia Pacific and Latin America schedules not yet configured) and the standing rule is to carry genuinely open items into the relevant page rather than leave them unrecorded.

## Anti-regression grep, actual hit counts

| Grep | Expected | Hits | Detail |
|---|---|---|---|
| `10:00`, `16:00`, `23:00`, `catch-up`, `multiple times per` | Zero in any fan-out context | 5 legitimate hits, all in `special-considerations/data-transmission-contingency.md`'s manual, semi-automated pilot upload schedule (a different, human-driven process, explicitly out of scope per the spec's own note); one `catch-up` mention inside this pass's own revision-log entry, quoting what was wrong for the historical record. Zero assertions that a catch-up or these times exist in the current fan-out or export schedule. | Left the contingency file's 5 hits deliberately; different process, own context. |
| `08:00`, `11:00`, `14:00`, `Europe/London` | Present, United Kingdom fan-out table | Present, twice: the table itself and the "use your own row" caution sentence | |
| `12:00`, `15:00`, `18:00`, `America/New_York` | Present, United States fan-out table and the two export-pipeline rows | Present: US fan-out table, both export-pipeline table rows (UK's export time is also `America/New_York`, per fact 118), and the caution sentence | |
| `safety net`, `backstop`, `fallback` near post-processing | Zero | 2 hits, both explicit denials ("not a fallback for something else", "not a fallback behind something faster"), matching the spec's own required wording; other `fallback` hits are the pre-existing, unrelated Run Options and Contingency CSV sections | Zero assertions that scheduled processing is secondary. |
| A promise that a Level 2.5 change lands in minutes | Zero | 0 after fixing `bu-sku-level-25-mode.md` and `forecast-reconciliation-template.md`; the only remaining "minutes" hits are the pre-existing, unrelated dashboard-refresh cadence and this pass's own corrective revision-log text | |
| Level 1 writes are immediate | Present | Present in `timing-system-sync.md`'s table and prose, and `batch-orchestration-updates.md`'s "in brief" note | |
| A single table mixing weekday fan-out rows with Friday or Saturday export rows | Zero | 0. Two separate tables under two separate headings in `timing-system-sync.md`; `batch-orchestration-updates.md` uses prose bullets for both, never a shared table | |
| A Level 1 user cannot see a Level 2.5 change, or must use the dashboard for it | Zero | 2 hits, both negations of the old claim, unaffected by this pass | |
| `PHASE_OUT` | Every list containing it also contains `NON_STATISTICAL_DEMAND` | Confirmed on all current lists, unaffected by this pass; two historical revision-log entries predating the type correctly excluded | |
| `NON_STATISTICAL_DEMAND` | Present in the array mapping, the enrichment capture template page and the glossary | Present in all three (plus two more), unaffected by this pass | |
| `Management Indicator` | Present in the glossary and in `workflows/forecast-range-calculation.md` | Present in both (plus two more), unaffected by this pass | |
| "No open questions were identified" on `fcr-adjustment-rules.md` | Zero | 0, unaffected by this pass | |

## `mkdocs build --strict`

Passes clean, no warnings.

## Consolidated manual

Regenerated with `tools/generate_manual_full.py`: **`HERO_Manual_Full_v8_2026-08-07.md`, 178,476 bytes, 29 nav pages**, at the repository root. This is the file that replaces the hand-corrected interim file currently loaded into the HERO assistant; the filename is unchanged from previous drops (the manual's own version number, v8, has not incremented; only its content has).

## Drop

Produced with `tools/make_drop.py` after committing, source commit matching the manifest. Not committed to the repo (gitignored by design, per the existing one-way drop convention); handed back separately.

## No PR #24 content reverted

`git diff main -- docs/index.md mkdocs.yml` is empty. The Power BI link PR #24 added (`1d7dcc05-0d12-40f8-bd0c-184b82bdd406`) is present, unchanged, in `docs/index.md`, `docs/tools/reference-views-dashboards.md`, `mkdocs.yml`, and the regenerated consolidated manual.

## Nav

Unchanged. No change in this pass needed a new page.
