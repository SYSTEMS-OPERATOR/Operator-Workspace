import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
from scipy.linalg import logm, expm
from e4d.e2 import Kernel


def test_bch_sl2():
    k = Kernel()
    a = k.encode(0.2)
    b = k.encode(-0.1)
    comp_kernel = k.compose(a, b)
    comp_ref = logm(expm(a) @ expm(b)).real
    assert np.allclose(comp_kernel, comp_ref, atol=1e-10)
