import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.qa_pipeline import unify_bibtex


def test_unify_bibtex_creates_key_map(tmp_path: Path) -> None:
    # setup temporary repository structure
    root = tmp_path
    (root / "docs" / "refs").mkdir(parents=True)
    # create two bib files with unique keys
    file_a = root / "a.bib"
    file_a.write_text("@book{refA, title={A}}\n")
    subdir = root / "sub"
    subdir.mkdir()
    file_b = subdir / "b.bib"
    file_b.write_text("@article{refB, title={B}}\n")

    key_map = unify_bibtex(root)

    # verify consolidated bib file exists
    bib_text = (root / "docs" / "refs" / "e_series.bib").read_text()
    assert "refA" in bib_text and "refB" in bib_text

    # verify key map json contents
    key_map_file = json.loads(
        (root / "docs" / "refs" / "e_series_keymap.json").read_text()
    )
    expected = {"refA": "a.bib", "refB": "sub/b.bib"}
    assert key_map == expected
    assert key_map_file == expected
