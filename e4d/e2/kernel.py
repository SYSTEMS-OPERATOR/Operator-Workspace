"""X-axis kernel implementing sl(2,R)."""

from __future__ import annotations

import numpy as np
from numpy import ndarray
from scipy.linalg import expm, logm

from ..base import AbstractBaseKernel, _bch

# Cartan element for sl(2)
_H = np.array([[0.5, 0.0], [0.0, -0.5]], dtype=float)


class Kernel(AbstractBaseKernel):
    """E2 kernel based on sl(2,R)."""

    def encode(self, q: float | ndarray) -> ndarray:
        q = float(np.squeeze(q))
        return q * _H

    def decode(self, v: ndarray) -> float:
        v = np.asarray(v, dtype=float)
        return float(v[0, 0] - v[1, 1])

    def evolve(self, v: ndarray, tau: float) -> ndarray:
        v = np.asarray(v, dtype=float)
        return expm(tau * v)

    def compose(self, *vs: ndarray) -> ndarray:
        result = np.asarray(vs[0], dtype=float)
        for nxt in vs[1:]:
            result = _bch(result, np.asarray(nxt, dtype=float))
        return result
