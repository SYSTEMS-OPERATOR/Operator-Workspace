from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.repo_inventory import build_manifest


def test_manifest_contains_inventory_script(tmp_path):
    manifest = build_manifest(Path.cwd())
    assert 'scripts/repo_inventory.py' in manifest['code']
