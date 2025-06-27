import numpy as np
from pathlib import Path

from lie_algebra import RootSystemGenerator


def test_a2_generation(tmp_path: Path) -> None:
    gen = RootSystemGenerator(cache_dir=tmp_path)
    roots = gen.roots("A2")
    assert roots.shape == (6, 3)
    roots2 = gen.roots("A2")
    assert np.array_equal(roots, roots2)


def test_d4_count(tmp_path: Path) -> None:
    gen = RootSystemGenerator(cache_dir=tmp_path)
    roots = gen.roots("D4")
    assert roots.shape == (24, 4)
