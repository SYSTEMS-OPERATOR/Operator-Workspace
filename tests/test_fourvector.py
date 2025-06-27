import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
import pytest
from e4d.bundle import FourVector


def minkowski_norm(v: FourVector) -> float:
    t, x, y, z = v._decode_components()
    return -t ** 2 + x ** 2 + y ** 2 + z ** 2


def test_lorentz_invariance():
    fv = FourVector(1.0, 0.2, -0.1, 0.3)
    norm_before = minkowski_norm(fv)
    boosted = fv.lorentz_boost(0.3, axis="x")
    norm_after = minkowski_norm(boosted)
    assert np.allclose(norm_before, norm_after, atol=1e-10)


def test_boost_axes():
    fv = FourVector(1.0, 0.2, -0.1, 0.3)
    for ax in ("x", "y", "z"):
        boosted = fv.lorentz_boost(0.1, axis=ax)
        assert np.allclose(minkowski_norm(fv), minkowski_norm(boosted), atol=1e-10)


def test_invalid_axis():
    fv = FourVector(1.0, 0.0, 0.0, 0.0)
    with pytest.raises(ValueError):
        fv.lorentz_boost(0.1, axis="w")
