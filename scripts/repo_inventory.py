"""Repository inventory utility."""

import argparse
import json
from pathlib import Path
from typing import Dict, List

EXT_MAP: Dict[str, List[str]] = {
    "code": [".py", ".ipynb", ".sage", ".m", ".jl"],
    "data": [".json", ".csv", ".npy", ".pkl"],
    "docs": [".md", ".pdf", ".tex", ".bib"],
}


def classify_file(path: Path) -> str | None:
    """Classify file by extension or CI location."""
    ci_file = path.match(".github/workflows/*.yml")
    ci_file |= path.name.startswith("Dockerfile")
    ci_file |= path.name.startswith("requirements")
    if ci_file:
        return "ci"
    for category, exts in EXT_MAP.items():
        if path.suffix in exts:
            return category
    return None


def build_manifest(root: Path) -> Dict[str, List[str]]:
    """Build manifest mapping categories to relative file paths."""
    manifest: Dict[str, List[str]] = {"code": [], "data": [], "docs": [], "ci": []}
    for file in root.rglob("*"):
        if not file.is_file():
            continue
        category = classify_file(file)
        if category:
            manifest[category].append(str(file.relative_to(root)))
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate repository manifest")
    parser.add_argument("--output", default="repo_manifest.json", help="Output manifest path")
    args = parser.parse_args()

    manifest = build_manifest(Path.cwd())
    with open(args.output, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)


if __name__ == "__main__":
    main()
