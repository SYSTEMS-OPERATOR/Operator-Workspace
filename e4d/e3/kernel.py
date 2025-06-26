import numpy as np
from numpy import ndarray

from ..base import AbstractBaseKernel, bch
from ..e2.kernel import H as H2

H3 = np.diag([1.0, -1.0, 0.0])


class Kernel(AbstractBaseKernel):
    """Y-axis kernel using sl(3) ⊕ sl(2)."""

    def encode(self, q: float | ndarray) -> ndarray:
        top = q * H3
        bottom = np.zeros_like(H2)
        return np.block([[top, np.zeros((3, 2))], [np.zeros((2, 3)), bottom]])

    def decode(self, v: ndarray) -> float | ndarray:
        return float(v[0, 0])

    def compose(self, *vs: ndarray) -> ndarray:
        result = vs[0]
        for v in vs[1:]:
            result = bch(result, v)
        return result

    def evolve(self, v: ndarray, tau: float) -> ndarray:
        generator = np.block([[tau * H3, np.zeros((3, 2))], [np.zeros((2, 3)), np.zeros_like(H2)]])
        return self.compose(v, generator)
