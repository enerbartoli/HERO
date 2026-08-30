#!/usr/bin/env python3
"""Produce a full repository archive, ``.git`` included.

This is a different artefact from ``make_drop.py``'s content drop. Its job is
to seed the *next* Claude Code session with real history — branches, commit
messages, the full log — instead of a content-only snapshot that looks
current but carries none of the "why". A drop answers "what did the manual
say on this day"; this answers "what do I clone to keep working on it".

Output name:
    HERO_Manual_Repo_gitincluded_<YYYY-MM-DD>_<short-sha>.zip

Stdlib only.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import subprocess
import sys
import zipfile

# Excluded only as top-level (repo-root) directories — NOT at any depth.
NEVER_TOP = {"site"}
# Excluded at any depth.
NEVER_ANY = {"__pycache__", ".venv", "venv", ".cache"}
NEVER_EXT = {".zip"}

DEFAULT_PREFIX = "HERO_Manual_Repo_gitincluded"
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


def collect_files(repo_root: str) -> list[str]:
    found = []
    for dirpath, dirnames, filenames in os.walk(repo_root):
        rel_dir = os.path.relpath(dirpath, repo_root).replace(os.sep, "/")
        parts = [] if rel_dir == "." else rel_dir.split("/")
        if parts and parts[0] in NEVER_TOP:
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if d not in NEVER_ANY]
        for fn in filenames:
            if os.path.splitext(fn)[1].lower() in NEVER_EXT:
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, repo_root).replace(os.sep, "/")
            found.append(rel)
    return sorted(found)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    repo_default = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    p.add_argument("--repo-root", default=repo_default)
    p.add_argument("--out-dir", default=repo_default,
                    help="Where to write the zip (default: repo root).")
    p.add_argument("--prefix", default=DEFAULT_PREFIX)
    p.add_argument("--dest", default=DEFAULT_DEST,
                    help="Destination folder to print (where you copy the archive).")
    p.add_argument("--date", default=None, help="YYYY-MM-DD (default: today).")
    args = p.parse_args(argv)

    repo_root = os.path.abspath(args.repo_root)
    out_dir = os.path.abspath(args.out_dir)
    date = args.date or _dt.date.today().isoformat()

    short_sha = git(repo_root, "rev-parse", "--short", "HEAD")

    files = collect_files(repo_root)
    if not files:
        sys.stderr.write("ERROR: nothing found to archive.\n")
        return 1

    os.makedirs(out_dir, exist_ok=True)
    zip_name = f"{args.prefix}_{date}_{short_sha}.zip"
    zip_path = os.path.join(out_dir, zip_name)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in files:
            z.write(os.path.join(repo_root, rel), rel)

    size = os.path.getsize(zip_path)
    print(f"Wrote {zip_name} ({len(files)} files, {size:,} bytes, HEAD {short_sha}, .git included).")
    print("")
    print("Copy this archive to (this folder is read-only and is NEVER edited):")
    print(f"  {args.dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
