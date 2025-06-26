"""Z-axis kernel using sl(5)."""

from __future__ import annotations

import numpy as np
from numpy import ndarray
from scipy.linalg import expm

from ..base import AbstractBaseKernel, _bch

_H5 = np.diag([0.4, 0.2, 0.0, -0.2, -0.4])


class Kernel(AbstractBaseKernel):
    """E4 kernel based on sl(5)."""

    def encode(self, q: float | ndarray) -> ndarray:
        q = float(np.squeeze(q))
        return q * _H5

    def decode(self, v: ndarray) -> float:
        v = np.asarray(v, dtype=float)
        return float((v[0, 0] - v[-1, -1]) / 0.8)

    def evolve(self, v: ndarray, tau: float) -> ndarray:
        v = np.asarray(v, dtype=float)
        return expm(tau * v)

    def compose(self, *vs: ndarray) -> ndarray:
        result = np.asarray(vs[0], dtype=float)
        for nxt in vs[1:]:
            result = _bch(result, np.asarray(nxt, dtype=float))
        return result
