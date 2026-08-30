#!/usr/bin/env python3
"""Generate the consolidated single-file manual from the MkDocs site.

The consolidated file (``HERO_Manual_Full_v<N>_<YYYY-MM-DD>.md`` at the repo
root) is the knowledge file for the Brave assistant. It USED to be maintained
by hand and fell a month behind the site; it is now generated from the site
source so it can never drift.

What it does:
  * reads ``mkdocs.yml``'s nav order,
  * concatenates every ``docs/**/*.md`` page in that order,
  * flattens the MkDocs ``!!! type "label"`` admonition syntax into plain
    Markdown so the file reads cleanly outside MkDocs,
  * writes the consolidated file at the repo root.

It fails loudly if a page under ``docs/`` is missing from the nav, or a nav
entry points at a file that does not exist — those are exactly the drifts this
generator exists to prevent.

Usage:
  python3 tools/generate_manual_full.py            # write the file
  python3 tools/generate_manual_full.py --check     # verify it is up to date
                                                     # (exit 1 if stale/missing)

The version and date are never hardcoded here, so neither can go stale by
being forgotten in this file:

  * the **version** is read from the ``VERSION`` file at the repo root — the
    one place a human bumps it, when the manual reaches a new published
    version;
  * the **date** is the wall-clock date of the run (nobody types it).

The output filename and the in-file header are always built from that same
pair, so they cannot disagree. ``--check`` finds the committed
``HERO_Manual_Full_v*.md``, reads the version/date back out of *its own
filename*, regenerates in memory using that exact pair, and compares — so the
check is a pure function of the committed state, not of today's date, and a
docs change that is not regenerated still fails it.

No third-party dependencies beyond PyYAML, which ships with MkDocs (already a
repo dependency via ``requirements.txt``).
"""

from __future__ import annotations

import argparse
import datetime
import glob
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover - environment guard
    sys.stderr.write(
        "ERROR: PyYAML is required (it ships with mkdocs). "
        "Run: pip install -r requirements.txt\n"
    )
    raise SystemExit(2)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
MKDOCS_YML = os.path.join(REPO_ROOT, "mkdocs.yml")
VERSION_FILE = os.path.join(REPO_ROOT, "VERSION")

PAGE_SEPARATOR = "\n\n---\n\n"

_ADMONITION_RE = re.compile(
    r'^(?P<indent>\s*)(?P<marker>!!!|\?\?\?\+?)\s+'
    r'(?P<type>[A-Za-z][\w-]*)'
    r'(?:\s+"(?P<title>.*)")?\s*$'
)
_FENCE_RE = re.compile(r'^\s*(```+|~~~+)')
_OUTPUT_GLOB = "HERO_Manual_Full_v*.md"
_OUTPUT_RE = re.compile(r'^HERO_Manual_Full_v(?P<version>[^_]+)_(?P<date>\d{4}-\d{2}-\d{2})\.md$')
_HEADER_RE = re.compile(r'^\*\*Version (?P<version>\S+) - (?P<date>\d{4}-\d{2}-\d{2})\*\*$', re.MULTILINE)


def read_repo_version() -> str:
    """The manual's published-version number, read from the one file that
    carries it. A human bumps this file when the manual reaches a new
    published version; nothing here should ever hardcode it again."""
    try:
        with open(VERSION_FILE, "r", encoding="utf-8") as fh:
            version = fh.read().strip()
    except FileNotFoundError:
        raise SystemExit(f"ERROR: {VERSION_FILE} is missing. Create it with the manual's version number.")
    if not version:
        raise SystemExit(f"ERROR: {VERSION_FILE} is empty.")
    return version


def today() -> str:
    """The build date. Nobody types this; it is always today."""
    return datetime.date.today().isoformat()


def output_filename(version: str, date: str) -> str:
    return f"HERO_Manual_Full_v{version}_{date}.md"


def find_committed_output():
    """The single committed ``HERO_Manual_Full_v*.md`` at the repo root, its
    version and date as read from its own filename. Used by ``--check`` so
    the check never depends on today's date, only on what is committed."""
    matches = sorted(glob.glob(os.path.join(REPO_ROOT, _OUTPUT_GLOB)))
    if not matches:
        return None
    if len(matches) > 1:
        names = ", ".join(os.path.basename(m) for m in matches)
        raise SystemExit(
            f"ERROR: more than one consolidated manual file at the repo root ({names}). "
            "Remove the stale one(s); exactly one should exist."
        )
    path = matches[0]
    name = os.path.basename(path)
    m = _OUTPUT_RE.match(name)
    if not m:
        raise SystemExit(f"ERROR: {name} does not match the expected HERO_Manual_Full_v<N>_<date>.md pattern.")
    return path, m.group("version"), m.group("date")


# ---------------------------------------------------------------------------
# mkdocs.yml nav walking
# ---------------------------------------------------------------------------
def _is_external_or_html(target: str) -> bool:
    """True for nav targets that are not local Markdown pages."""
    lowered = target.strip().lower()
    if lowered.startswith(("http://", "https://")):
        return True
    if lowered.endswith(".html"):
        return True
    return False


def _walk_nav(node, out):
    """Collect docs-relative .md paths from a mkdocs nav node, in order."""
    if isinstance(node, list):
        for item in node:
            _walk_nav(item, out)
    elif isinstance(node, dict):
        for _title, value in node.items():
            _walk_nav(value, out)
    elif isinstance(node, str):
        if not _is_external_or_html(node):
            out.append(node)


def load_nav_pages():
    with open(MKDOCS_YML, "r", encoding="utf-8") as fh:
        config = yaml.safe_load(fh)
    nav = config.get("nav")
    if not nav:
        raise SystemExit("ERROR: mkdocs.yml has no `nav` section to read.")
    pages = []
    _walk_nav(nav, pages)
    return pages


def discover_docs_md():
    """All docs/**/*.md paths, docs-relative, using forward slashes."""
    found = []
    for dirpath, _dirs, files in os.walk(DOCS_DIR):
        for name in files:
            if name.endswith(".md"):
                full = os.path.join(dirpath, name)
                rel = os.path.relpath(full, DOCS_DIR).replace(os.sep, "/")
                found.append(rel)
    return set(found)


def validate(nav_pages):
    """Fail loudly on nav/docs mismatch. Returns nav_pages unchanged."""
    nav_set = set(nav_pages)
    docs_set = discover_docs_md()

    missing_files = [p for p in nav_pages if not os.path.isfile(os.path.join(DOCS_DIR, p))]
    orphan_pages = sorted(docs_set - nav_set)

    problems = []
    if missing_files:
        problems.append(
            "Nav entries point at files that do not exist under docs/:\n  - "
            + "\n  - ".join(missing_files)
        )
    if orphan_pages:
        problems.append(
            "Pages under docs/ are missing from the mkdocs.yml nav:\n  - "
            + "\n  - ".join(orphan_pages)
        )
    if problems:
        raise SystemExit("ERROR: docs/nav are out of sync.\n\n" + "\n\n".join(problems))
    return nav_pages


# ---------------------------------------------------------------------------
# Admonition flattening
# ---------------------------------------------------------------------------
def _strip_leading(line: str, n: int) -> str:
    """Remove up to n leading spaces from line."""
    i = 0
    while i < n and i < len(line) and line[i] == " ":
        i += 1
    return line[i:]


def flatten_admonitions(text: str) -> str:
    """Turn MkDocs ``!!! type "Title"`` blocks into plain Markdown.

    The marker becomes a bold label (``**Type — Title**``) and the 4-space
    indented body is de-indented back to the margin so tables and lists render.
    Nested admonitions de-indent one level per enclosing block. Content inside
    fenced code blocks is de-indented but never interpreted as a marker.
    """
    lines = text.splitlines()
    out = []
    stack = []          # indentation (int) of each open admonition marker
    in_fence = False

    for line in lines:
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))

        # Close any admonitions this (non-blank) line has dedented out of.
        if stripped and not in_fence:
            while stack and indent <= stack[-1]:
                stack.pop()

        reduce = 4 * len(stack)

        # Fence toggle (after close-check so the closing fence de-indents too).
        if _FENCE_RE.match(line):
            out.append(_strip_leading(line, reduce))
            in_fence = not in_fence
            continue

        if in_fence:
            out.append(_strip_leading(line, reduce))
            continue

        m = _ADMONITION_RE.match(line)
        if m:
            label_type = m.group("type").capitalize()
            title = m.group("title")
            label = f"**{label_type} — {title}**" if title else f"**{label_type}**"
            # Keep the label at the marker's own column (minus any enclosing
            # admonition reductions) so an admonition nested inside a list item
            # stays aligned with its de-indented body instead of turning into
            # a stray indented code block.
            label_indent = max(0, indent - reduce)
            out.append(" " * label_indent + label)
            out.append("")  # blank line so the body is its own paragraph
            stack.append(indent)
            continue

        out.append(_strip_leading(line, reduce))

    return "\n".join(out).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------
def build_manual(version: str, date: str) -> str:
    nav_pages = validate(load_nav_pages())

    header = (
        "<!--\n"
        "  HERO User Manual - consolidated single-file export.\n"
        "  GENERATED FILE - do not edit by hand.\n"
        "  Regenerate with: python3 tools/generate_manual_full.py\n"
        "  Source of truth: the docs/ tree and the mkdocs.yml nav order.\n"
        "-->\n\n"
        "# HERO User Manual - Full Consolidated Manual\n\n"
        f"**Version {version} - {date}**\n\n"
        "This file concatenates every page of the HERO User Manual in nav "
        "order, with MkDocs admonition syntax flattened to plain Markdown. It "
        "is generated from the site source; do not edit it by hand "
        "(see README.md)."
    )

    parts = [header]
    for rel in nav_pages:
        with open(os.path.join(DOCS_DIR, rel), "r", encoding="utf-8") as fh:
            body = fh.read()
        parts.append(flatten_admonitions(body).rstrip())

    return PAGE_SEPARATOR.join(parts).rstrip() + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify the committed consolidated file is up to date; exit 1 if not.",
    )
    parser.add_argument(
        "--version",
        default=None,
        help="Override the version (default: read from the VERSION file).",
    )
    parser.add_argument(
        "--date",
        default=None,
        help="Override the date, YYYY-MM-DD (default: today; ignored by --check, "
        "which always uses the committed file's own date).",
    )
    args = parser.parse_args(argv)

    if args.check:
        found = find_committed_output()
        if found is None:
            sys.stderr.write(
                f"ERROR: no {_OUTPUT_GLOB} found at the repo root. "
                f"Regenerate with: python3 tools/generate_manual_full.py\n"
            )
            return 1
        out_path, version, date = found
        rel_out = os.path.relpath(out_path, REPO_ROOT)

        with open(out_path, "r", encoding="utf-8") as fh:
            current = fh.read()

        header_match = _HEADER_RE.search(current)
        if not header_match or header_match.group("version") != version or header_match.group("date") != date:
            sys.stderr.write(
                f"ERROR: {rel_out}'s filename says version {version} / {date}, but its own "
                f"header does not say the same thing. Regenerate; never hand-edit either.\n"
            )
            return 1

        content = build_manual(version, date)
        if current != content:
            sys.stderr.write(
                f"ERROR: {rel_out} is out of date with respect to docs/.\n"
                f"Regenerate with: python3 tools/generate_manual_full.py "
                f"and commit the result. Never edit it by hand.\n"
            )
            return 1
        print(f"OK: {rel_out} is up to date ({len(load_nav_pages())} nav pages).")
        return 0

    version = args.version or read_repo_version()
    date = args.date or today()
    content = build_manual(version, date)
    out_path = os.path.join(REPO_ROOT, output_filename(version, date))
    rel_out = os.path.relpath(out_path, REPO_ROOT)

    # Exactly one consolidated manual file should exist at the repo root, so a
    # stale version/date can never sit next to the current one.
    for stale in glob.glob(os.path.join(REPO_ROOT, _OUTPUT_GLOB)):
        if os.path.abspath(stale) != os.path.abspath(out_path):
            os.remove(stale)
            print(f"Removed stale {os.path.relpath(stale, REPO_ROOT)}.")

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"Wrote {rel_out} ({len(content):,} bytes, {len(load_nav_pages())} nav pages).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
