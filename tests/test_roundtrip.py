"""Encode-decode round-trip accuracy tests."""

import sys
from pathlib import Path
import numpy as np
from numpy.testing import assert_allclose

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from e4d.e1 import Kernel as E1
from e4d.e2 import Kernel as E2
from e4d.e3 import Kernel as E3
from e4d.e4 import Kernel as E4


def _roundtrip(kernel, value):
    encoded = kernel.encode(value)
    decoded = kernel.decode(encoded)
    assert_allclose(decoded, value, rtol=1e-12, atol=1e-12)


def test_e1_roundtrip():
    _roundtrip(E1(), 3.14)


def test_e2_roundtrip():
    _roundtrip(E2(), 1.23)


def test_e3_roundtrip():
    _roundtrip(E3(), -0.5)


def test_e4_roundtrip():
    _roundtrip(E4(), 2.0)
