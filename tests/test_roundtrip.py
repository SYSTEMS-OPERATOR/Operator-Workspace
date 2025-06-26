import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
from e4d.e1 import Kernel as E1
from e4d.e2 import Kernel as E2
from e4d.e3 import Kernel as E3
from e4d.e4 import Kernel as E4


def _roundtrip(kernel):
    q = np.random.rand()
    encoded = kernel.encode(q)
    decoded = kernel.decode(encoded)
    assert np.allclose(q, decoded, rtol=1e-12)


def test_roundtrip_e1():
    _roundtrip(E1())


def test_roundtrip_e2():
    _roundtrip(E2())


def test_roundtrip_e3():
    _roundtrip(E3())


def test_roundtrip_e4():
    _roundtrip(E4())
