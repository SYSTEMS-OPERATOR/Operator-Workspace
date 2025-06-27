"""Utility script to scan repository and detect duplicate files."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]

CATEGORIES = {
    "code": {".py", ".ipynb", ".sage", ".m", ".jl"},
    "data": {".json", ".csv", ".npy", ".pkl"},
    "docs": {".md", ".pdf", ".tex", ".bib"},
    "ci": {".yml", "Dockerfile"},
}


def sha256(path: Path) -> str:
    """Compute SHA256 for a file."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def scan_repo(root: Path = ROOT) -> Dict[str, List[str]]:
    """Walk repository and classify files."""
    manifest: Dict[str, List[str]] = {k: [] for k in CATEGORIES}
    manifest["other"] = []
    for path in root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            ext = path.suffix
            added = False
            for cat, exts in CATEGORIES.items():
                if ext in exts:
                    manifest[cat].append(str(path.relative_to(root)))
                    added = True
                    break
            if not added:
                manifest["other"].append(str(path.relative_to(root)))
    return manifest


def detect_duplicates(paths: List[str], root: Path = ROOT) -> Dict[str, List[str]]:
    """Return mapping of ``sha256`` to file paths for duplicates.

    Parameters
    ----------
    paths:
        File paths relative to ``root``.
    root:
        Base directory for resolving ``paths``.
    """

    hashes: Dict[str, List[str]] = {}
    for p in paths:
        full_path = root / p
        h = sha256(full_path)
        hashes.setdefault(h, []).append(p)
    return {h: ps for h, ps in hashes.items() if len(ps) > 1}


def main() -> None:
    manifest = scan_repo()
    with open("repo_manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    dups = detect_duplicates([p for group in manifest.values() for p in group], ROOT)
    if dups:
        with open("duplicate_files.json", "w", encoding="utf-8") as f:
            json.dump(dups, f, indent=2)
    print("Manifest written with", sum(len(v) for v in manifest.values()), "files")
    if dups:
        print("Duplicates detected:", len(dups))


if __name__ == "__main__":
    main()
