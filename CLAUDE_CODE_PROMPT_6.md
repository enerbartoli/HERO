# Prompt 6 for Claude Code — replace the BU-SKU worked-examples page (readability fix)

The page `docs/examples/bu-sku-worked-examples.md` was **rewritten** to be readable: the dense
number-soup paragraphs are replaced with a before/after **table** per scenario plus a one-line
"Takeaway" callout. I'm sharing the updated file alongside this prompt.

## What to do
1. **Replace** `docs/examples/bu-sku-worked-examples.md` in the repo with the version I shared
   (overwrite it entirely — the new content is correct and final).
2. Do **not** rewrite, re-summarise, or "tidy" the content. Keep the tables and the `!!! note`
   "Takeaway" / `!!! tip` / `!!! success` admonitions exactly as written.
3. Confirm the Markdown tables render under Material (right-aligned numeric columns using `--:`).
4. Re-run `mkdocs build --strict` — expect 0 warnings.
5. Check no stray NUL/control bytes: `grep -lP '\x00' docs/examples/bu-sku-worked-examples.md`
   should return nothing.

## Constraints (unchanged)
- Tool-focus content; do not reintroduce pilot-specific material.
- This page ends with `!!! success "No open questions identified"` — keep it; do not add gaps.

## Report
Confirm the build passes and paste/screenshot the rendered Example 1 and Example 4 tables so we can
see the before/after layout is clear.
