import numpy as np
from numpy import ndarray

from ..base import AbstractBaseKernel, bch

H4 = np.diag([1.0, -1.0, 0.0, 0.0, 0.0])


class Kernel(AbstractBaseKernel):
    """Z-axis kernel using sl(5)."""

    def encode(self, q: float | ndarray) -> ndarray:
        return q * H4

    def decode(self, v: ndarray) -> float | ndarray:
        return float(v[0, 0])

    def compose(self, *vs: ndarray) -> ndarray:
        result = vs[0]
        for v in vs[1:]:
            result = bch(result, v)
        return result

    def evolve(self, v: ndarray, tau: float) -> ndarray:
        return self.compose(v, tau * H4)
