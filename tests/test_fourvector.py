"""Minkowski norm invariance under Lorentz boosts."""

import sys
from pathlib import Path
import numpy as np
from numpy.testing import assert_allclose

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from e4d.bundle import FourVector


def test_minkowski_invariance():
    fv = FourVector.from_scalars(2.0, 0.5, -0.1, 0.0)
    norm_before = fv.minkowski_norm()
    boosted = fv.lorentz_boost(0.3, axis="x")
    norm_after = boosted.minkowski_norm()
    assert_allclose(norm_after, norm_before, rtol=1e-12, atol=1e-12)
