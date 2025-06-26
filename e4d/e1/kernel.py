"""Time kernel implementing the E1 algebra."""

from __future__ import annotations

import numpy as np
from numpy import ndarray

from ..base import AbstractBaseKernel


class Kernel(AbstractBaseKernel):
    """E1 time kernel (abelian)."""

    def encode(self, q: float | ndarray) -> ndarray:
        return np.atleast_1d(q).astype(float)

    def decode(self, v: ndarray) -> float | ndarray:
        v = np.asarray(v, dtype=float)
        return v[0] if v.size == 1 else v

    def evolve(self, v: ndarray, tau: float) -> ndarray:
        return np.asarray(v, dtype=float) + tau

    def compose(self, *vs: ndarray) -> ndarray:
        return sum(np.asarray(v, dtype=float) for v in vs)
