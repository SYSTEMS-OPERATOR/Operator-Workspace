"""Repository QA integration utilities."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Dict, List

import yaml


CATEGORIES = {
    "code": {".py", ".ipynb", ".sage", ".m", ".jl"},
    "data": {".json", ".csv", ".npy", ".pkl"},
    "docs": {".md", ".pdf", ".tex", ".bib"},
    "ci": {"Dockerfile"},
}


def scan_repo(root: Path) -> Dict[str, List[str]]:
    """Walk the repository and categorise files by extension."""
    manifest: Dict[str, List[str]] = {key: [] for key in CATEGORIES}
    manifest["ci"].extend(
        str(p)
        for p in (root / ".github" / "workflows").glob("*.yml")
        if p.is_file()
    )
    for path in root.rglob("*"):
        if path.is_file():
            ext = path.suffix
            for category, exts in CATEGORIES.items():
                if ext in exts:
                    manifest[category].append(str(path.relative_to(root)))
                    break
    with open(root / "repo_manifest.yaml", "w", encoding="utf-8") as fh:
        yaml.safe_dump(manifest, fh, sort_keys=False)
    return manifest


def detect_duplicates(paths: List[str]) -> Dict[str, List[str]]:
    """Find exact duplicate files by SHA256."""
    hashes: Dict[str, List[str]] = {}
    for path in paths:
        with open(path, "rb") as fh:
            digest = hashlib.sha256(fh.read()).hexdigest()
        hashes.setdefault(digest, []).append(path)
    return {h: ps for h, ps in hashes.items() if len(ps) > 1}


def unify_bibtex(root: Path) -> None:
    """Combine BibTeX files into ``docs/refs/e_series.bib``."""
    refs_dir = root / "docs" / "refs"
    refs_dir.mkdir(parents=True, exist_ok=True)
    bib_files = list(root.rglob("*.bib"))
    if not bib_files:
        (refs_dir / "e_series.bib").write_text("% Consolidated references\n")
        return

    seen: set[str] = set()
    with open(refs_dir / "e_series.bib", "w", encoding="utf-8") as out:
        for file in bib_files:
            for line in file.read_text().splitlines():
                if line.startswith("@"):
                    key = line.split("{", 1)[1].split(",", 1)[0]
                    if key in seen:
                        continue
                    seen.add(key)
                out.write(line + "\n")


if __name__ == "__main__":  # pragma: no cover - simple CLI
    ROOT = Path(__file__).resolve().parents[1]
    manifest = scan_repo(ROOT)
    duplicates = detect_duplicates(
        [str(Path(ROOT, p)) for paths in manifest.values() for p in paths]
    )
    unify_bibtex(ROOT)
    print(json.dumps({"duplicates": duplicates}, indent=2))
