import numpy as np
from numpy import ndarray

from ..base import AbstractBaseKernel


class Kernel(AbstractBaseKernel):
    """Time kernel for the E1 algebra."""

    def encode(self, q: float | ndarray) -> ndarray:
        return np.array([q], dtype=float)

    def decode(self, v: ndarray) -> float | ndarray:
        return float(v[0])

    def compose(self, *vs: ndarray) -> ndarray:
        return np.array([sum(v[0] for v in vs)], dtype=float)

    def evolve(self, v: ndarray, tau: float) -> ndarray:
        return self.compose(v, np.array([tau]))
