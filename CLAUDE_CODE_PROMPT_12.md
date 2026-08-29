# Prompt 12 — Four Canonical Facts sections into the manual (2026-08-28)

You are working in the `HERO` repository, the MkDocs Material site for the HERO user manual. Everything you need is in this repo. Do not look outside it.

## Context you need before you touch anything

The manual is **four Canonical Facts sections behind**: 17 (26 August), 18 (27 August), 19 (28 August) and 20 (28 August). Facts 94 to 127. Three previous update passes never reached the site, so this is a catch-up, not an increment.

Two of the changes are **corrections to content that is actively wrong**, not additions. Users are acting on both today:

1. The fan-out schedule on two pages describes a timetable that does not exist.
2. The manual tells Level 1 users they cannot see a Level 2.5 adjustment in their template. They can.

Start with those two.

## Read in this order

1. `update_kit/_KIT_README.md` — what each file in the kit is and how much authority it carries.
2. `update_kit/CHANGES_SPEC.md` — **the work order.** Thirteen changes, each naming the pages it touches.
3. `update_kit/HERO_Canonical_Facts_OnePager_v11_2026-08-28.txt` — the source of truth. Where the manual and this file disagree, this file wins.
4. `CLAUDE_CODE_START_HERE.md` — the standing constraints for this repo. They still apply.
5. `BRAND_ASSETS.md` — only if you touch anything presentational. You should not need to.

The other files in `update_kit/` are evidence. Read them when the spec points you at them, not before.

## Execute

Work through `CHANGES_SPEC.md` in order. Change 1 first, it is flagged as such in the spec.

The spec gives you the page paths and, where the current text is wrong, quotes it so you can find it. Several changes also ask you to grep the whole `docs/` tree, because the same wrong figure or the same superseded claim appears in more than one place. Do those greps. A correction that lands on one page and misses another is worse than no correction, because the two pages then disagree.

## Hard constraints

These are the standing repo rules plus the ones this pass adds.

- **You may write content this time, and only from the kit.** Previous prompts forbade authoring manual content. This one requires it, because the spec lands facts the manual does not carry. The constraint that replaces it: every sentence you add must trace to a file in `update_kit/`. If it does not, it does not go in.
- **Never invent a fact, an owner, a date, a threshold or a number.** Anything missing, contradictory, or that needs a real fact goes into `BUILD_NOTES.md` for Rene, or into an inline `<!-- TODO: confirm with Rene -->` where the spec says so. The spec already carries three of those; do not silently resolve them.
- **Do not restate product behaviour that belongs to the HERO product team.** `update_kit/HERO_BRAVE_Knowledge_Base_repo.txt` is their own controlled pack and it changes with the code. Cross-reference it, do not copy it into the manual. A second, staler copy is exactly the failure this pass exists to prevent.
- **Preserve every `!!! question "Gaps & Open Questions"` block**, except the one on `special-considerations/fcr-adjustment-rules.md` that change 5 explicitly replaces.
- **Do not change the nav** unless a change requires a new page. If one does, stop and record it in `BUILD_NOTES.md` before proceeding.
- **Nothing here is a commitment.** Accuracy figures, horizons and dates are directional findings. Do not let a date read as a promise.
- **No em-dashes** in prose you write. Commas, periods or parentheses.
- Keep MkDocs Material conventions: admonitions, tables, relative links.

## A note on tone, because this pass carries corrections

Two changes correct guidance the manual gave confidently. Write the corrected pages as though they had always said the right thing. Do not add "previously we said", "this has been updated", or changelog commentary in the body of a page. The revision log in `docs/reference/documentation-governance.md` is where that belongs, and change 13 asks you to write it there.

The one exception is change 8b, where the spec deliberately asks for a visible note telling users that a behaviour they can observe today is a known build gap and not their own error. Keep that one calm and short.

## Definition of done

- All thirteen changes in `CHANGES_SPEC.md` applied, or a precise list of which ones you could not complete and why.
- Every grep the spec asks for actually run, with the hits fixed. Report the hit count per grep.
- `mkdocs build --strict` passes, or a precise list of blockers.
- Consolidated manual regenerated with `tools/generate_manual_full.py`.
- Drop produced with `tools/make_drop.py`.
- `BUILD_NOTES.md` lists: every `<!-- TODO: confirm with Rene -->` you placed and where, anything in the spec you could not source from the kit, and any page where the spec and the existing text conflicted in a way you had to resolve by judgement.
- Committed on a branch and a pull request opened. Do not push to `main` directly.
- Report the live URL and the local `mkdocs serve` URL.

## Report back

When you finish, give a short summary in this shape:

1. What changed, by page, one line each.
2. The grep results: what you searched for, how many hits, how many fixed.
3. Anything you could not do, and what you need from Rene to finish it.
4. The `<!-- TODO: confirm with Rene -->` list.
5. Build status and the PR link.

No preamble, no restatement of the spec. Rene wrote it and does not need it read back.
