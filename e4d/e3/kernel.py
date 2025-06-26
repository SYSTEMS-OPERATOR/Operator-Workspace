"""Y-axis kernel using sl(3) \oplus sl(2)."""

from __future__ import annotations

import numpy as np
from numpy import ndarray
from scipy.linalg import expm

from ..base import AbstractBaseKernel, _bch

# Cartan elements
_H3 = np.diag([2.0 / 3.0, -1.0 / 3.0, -1.0 / 3.0])
_H2 = np.array([[0.5, 0.0], [0.0, -0.5]], dtype=float)


class Kernel(AbstractBaseKernel):
    """E3 kernel based on sl(3) ⊕ sl(2)."""

    def encode(self, q: float | ndarray) -> ndarray:
        q = float(np.squeeze(q))
        top = q * _H3
        bottom = np.zeros_like(_H2)
        return np.block([[top, np.zeros((3, 2))], [np.zeros((2, 3)), bottom]])

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
