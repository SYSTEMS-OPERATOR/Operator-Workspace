from pathlib import Path
from scripts.repo_integrator import detect_duplicates


def test_detect_duplicates_resolves_relative_paths(tmp_path: Path) -> None:
    root = tmp_path
    file_a = root / "a.txt"
    file_b = root / "b.txt"
    file_a.write_text("same")
    file_b.write_text("same")
    duplicates = detect_duplicates(["a.txt", "b.txt"], root)
    assert any(len(paths) == 2 for paths in duplicates.values())
