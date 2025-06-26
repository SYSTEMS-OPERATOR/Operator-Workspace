import numpy as np
from numpy import ndarray
from scipy.linalg import expm

from ..base import AbstractBaseKernel, bch


H = np.array([[1.0, 0.0], [0.0, -1.0]])


class Kernel(AbstractBaseKernel):
    """X-axis kernel based on sl(2)."""

    def encode(self, q: float | ndarray) -> ndarray:
        return q * H

    def decode(self, v: ndarray) -> float | ndarray:
        return float(v[0, 0])

    def compose(self, *vs: ndarray) -> ndarray:
        result = vs[0]
        for v in vs[1:]:
            result = bch(result, v)
        return result

    def evolve(self, v: ndarray, tau: float) -> ndarray:
        return self.compose(v, tau * H)
