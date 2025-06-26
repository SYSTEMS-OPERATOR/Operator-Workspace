"""Synthesis layer for handling 4-vectors."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy import ndarray

from ..e1 import Kernel as TKernel
from ..e2 import Kernel as XKernel
from ..e3 import Kernel as YKernel
from ..e4 import Kernel as ZKernel


def _minkowski_norm(t: float, x: float, y: float, z: float) -> float:
    return t**2 - x**2 - y**2 - z**2


@dataclass
class FourVector:
    """Four-vector encoded via E-series kernels."""

    t: ndarray
    x: ndarray
    y: ndarray
    z: ndarray

    @classmethod
    def from_scalars(cls, t: float, x: float, y: float, z: float) -> "FourVector":
        return cls(TKernel().encode(t), XKernel().encode(x),
                   YKernel().encode(y), ZKernel().encode(z))

    def lorentz_boost(self, beta: float, axis: str = "x") -> "FourVector":
        gamma = 1.0 / np.sqrt(1 - beta**2)
        t_val, x_val, y_val, z_val = self.as_scalars()
        if axis == "x":
            t_prime = gamma * (t_val - beta * x_val)
            x_prime = gamma * (x_val - beta * t_val)
            y_prime, z_prime = y_val, z_val
        else:
            t_prime, x_prime, y_prime, z_prime = t_val, x_val, y_val, z_val
        return FourVector.from_scalars(t_prime, x_prime, y_prime, z_prime)

    def as_array(self) -> ndarray:
        return np.hstack([
            self.t.flatten(),
            self.x.flatten(),
            self.y.flatten(),
            self.z.flatten(),
        ])

    def as_scalars(self) -> tuple[float, float, float, float]:
        return (
            TKernel().decode(self.t),
            XKernel().decode(self.x),
            YKernel().decode(self.y),
            ZKernel().decode(self.z),
        )

    def minkowski_norm(self) -> float:
        t, x, y, z = self.as_scalars()
        return _minkowski_norm(t, x, y, z)

__all__ = ["FourVector"]
