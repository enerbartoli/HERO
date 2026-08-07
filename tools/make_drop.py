#!/usr/bin/env python3
"""Produce a one-way delivery drop (a full snapshot zip) of a repository.

The repository is the single source of truth. After each merge to ``main`` we
generate a zip snapshot of the publishable content and copy it, by hand, into a
read-only folder the process owner (and the Brave assistant) reads from. The
drop is never a source and is never edited: it is a coherent snapshot of the
repo at one commit, not an accumulation of patches.

This replaces the retired live-mirror script. It is parameterised so the same
tool drops other repositories (see ``--include`` / ``--dest`` and the
mod1-knowledge-check example in the README).

Output name:
    <prefix>_<YYYY-MM-DD>_<short-sha>.zip

The zip carries, at its root, a ``_DROP_MANIFEST.md`` stating that it is a
read-only copy, the repo URL / commit / date, what changed since the previous
drop, and the file list.

Stdlib only.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import fnmatch
import os
import re
import subprocess
import sys
import zipfile

# Excluded only as top-level (repo-root) directories — NOT at any depth, so a
# legitimate nested path like docs/tools/ is kept.
NEVER_TOP = {".git", ".github", "site", "tools"}
# Excluded at any depth.
NEVER_ANY = {"__pycache__"}
NEVER_GLOBS = ["*.zip"]

# Defaults for the HERO manual repo.
DEFAULT_INCLUDE = ["docs", "mkdocs.yml", "README.md", "HERO_Manual_Full_v*.md"]
DEFAULT_PREFIX = "HERO_Manual_Site_drop"
DEFAULT_DEST = (
    r"C:\Users\bartolr\OneDrive - Hasbro Inc\Demand Planning\HERO PROJECT"
    r"\04_outputs\_repo_snapshots\manual-site\\"
)


def git(repo_root, *args):
    out = subprocess.run(
        ["git", "-C", repo_root, *args],
        check=True, capture_output=True, text=True,
    )
    return out.stdout.strip()


def _excluded(rel_path: str) -> bool:
    parts = rel_path.replace("\\", "/").split("/")
    if parts[0] in NEVER_TOP:
        return True
    if any(p in NEVER_ANY for p in parts):
        return True
    name = parts[-1]
    return any(fnmatch.fnmatch(name, g) for g in NEVER_GLOBS)


def collect_files(repo_root: str, includes) -> list[str]:
    """Expand include patterns into a sorted list of repo-relative files."""
    found: set[str] = set()
    for pattern in includes:
        # Glob relative to the repo root (supports KC_..._v*.json style patterns).
        matches = _glob(repo_root, pattern)
        for m in matches:
            rel = os.path.relpath(m, repo_root).replace(os.sep, "/")
            if os.path.isdir(m):
                for dirpath, dirnames, filenames in os.walk(m):
                    dirnames[:] = [d for d in dirnames if d not in NEVER_ANY]
                    for fn in filenames:
                        full = os.path.join(dirpath, fn)
                        r = os.path.relpath(full, repo_root).replace(os.sep, "/")
                        if not _excluded(r):
                            found.add(r)
            else:
                if not _excluded(rel):
                    found.add(rel)
    return sorted(found)


def _glob(repo_root: str, pattern: str):
    import glob as _g
    return _g.glob(os.path.join(repo_root, pattern))


def previous_sha(out_dir: str, prefix: str) -> str | None:
    """Read the newest existing drop in out_dir and extract its source SHA."""
    if not os.path.isdir(out_dir):
        return None
    candidates = [
        os.path.join(out_dir, f)
        for f in os.listdir(out_dir)
        if fnmatch.fnmatch(f, f"{prefix}_*.zip")
    ]
    if not candidates:
        return None
    newest = max(candidates, key=os.path.getmtime)
    try:
        with zipfile.ZipFile(newest) as z:
            manifest = z.read("_DROP_MANIFEST.md").decode("utf-8", "replace")
        m = re.search(r"Source commit \(full\):\s*`?([0-9a-f]{7,40})`?", manifest)
        return m.group(1) if m else None
    except Exception:
        return None


def build_manifest(repo_root, repo_url, full_sha, message, date, since, files):
    lines = []
    lines.append("# Drop manifest — READ-ONLY COPY")
    lines.append("")
    lines.append(
        "This folder/zip is a **read-only copy generated from the repository**. "
        "Do not edit it — the **repository is the single source of truth**; any "
        "edit made here is not tracked and is lost on the next drop."
    )
    lines.append("")
    lines.append(f"- Repository: {repo_url}")
    lines.append(f"- Source commit (full): `{full_sha}`")
    lines.append(f"- Source commit message: {message}")
    lines.append(f"- Drop date: {date}")
    lines.append("")
    lines.append("## What changed since the previous drop")
    lines.append("")
    if since:
        log = git(repo_root, "log", "--pretty=- %s", f"{since}..{full_sha}")
        lines.append(log if log.strip() else "- No commits since the previous drop.")
    else:
        lines.append("- First drop — full snapshot; no previous drop to compare against.")
    lines.append("")
    lines.append("## Files included")
    lines.append("")
    for f in files:
        lines.append(f"- {f}")
    lines.append("")
    return "\n".join(lines)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    repo_default = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p.add_argument("--repo-root", default=repo_default)
    p.add_argument("--out-dir", default=repo_default,
                   help="Where to write the zip (default: repo root).")
    p.add_argument("--include", nargs="+", default=DEFAULT_INCLUDE,
                   help="Repo-relative files/dirs/globs to include.")
    p.add_argument("--prefix", default=DEFAULT_PREFIX)
    p.add_argument("--dest", default=DEFAULT_DEST,
                   help="Destination folder to print (where you copy the drop).")
    p.add_argument("--date", default=None, help="YYYY-MM-DD (default: today).")
    p.add_argument("--since", default=None,
                   help="Previous drop's commit SHA for the changelog "
                        "(default: auto-detected from the newest drop in --out-dir).")
    args = p.parse_args(argv)

    repo_root = os.path.abspath(args.repo_root)
    out_dir = os.path.abspath(args.out_dir)
    date = args.date or _dt.date.today().isoformat()

    full_sha = git(repo_root, "rev-parse", "HEAD")
    short_sha = git(repo_root, "rev-parse", "--short", "HEAD")
    message = git(repo_root, "log", "-1", "--pretty=%s")
    try:
        repo_url = git(repo_root, "remote", "get-url", "origin")
    except subprocess.CalledProcessError:
        repo_url = "(no origin remote)"

    files = collect_files(repo_root, args.include)
    if not files:
        sys.stderr.write("ERROR: nothing matched --include; refusing to make an empty drop.\n")
        return 1

    since = args.since or previous_sha(out_dir, args.prefix)
    manifest = build_manifest(repo_root, repo_url, full_sha, message, date, since, files)

    os.makedirs(out_dir, exist_ok=True)
    zip_name = f"{args.prefix}_{date}_{short_sha}.zip"
    zip_path = os.path.join(out_dir, zip_name)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("_DROP_MANIFEST.md", manifest)
        for rel in files:
            z.write(os.path.join(repo_root, rel), rel)

    print(f"Wrote {zip_name} ({len(files)} files, source commit {short_sha}).")
    print("")
    print("Copy this drop to (this folder is read-only and is NEVER edited):")
    print(f"  {args.dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
