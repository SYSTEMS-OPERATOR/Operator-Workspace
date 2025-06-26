"""Validate BCH composition for sl(2,R)."""

import sys
from pathlib import Path
import numpy as np
from numpy.testing import assert_allclose
from scipy.linalg import expm, logm

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from e4d.e2 import Kernel


def test_bch_compose():
    k = Kernel()
    a = k.encode(0.2)
    b = k.encode(-0.3)
    composed = k.compose(a, b)
    reference = logm(expm(a) @ expm(b)).real
    assert_allclose(composed, reference, rtol=1e-12, atol=1e-12)
