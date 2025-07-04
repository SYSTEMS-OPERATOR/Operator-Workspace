import numpy as np
from numpy import ndarray

from ..e1 import Kernel as TKernel
from ..e2 import Kernel as XKernel
from ..e3 import Kernel as YKernel
from ..e4 import Kernel as ZKernel


class FourVector:
    """Simple four-vector built from E-series kernels."""

    def __init__(self, t: float, x: float, y: float, z: float):
        self.t_kernel = TKernel()
        self.x_kernel = XKernel()
        self.y_kernel = YKernel()
        self.z_kernel = ZKernel()
        self.t = self.t_kernel.encode(t)
        self.x = self.x_kernel.encode(x)
        self.y = self.y_kernel.encode(y)
        self.z = self.z_kernel.encode(z)

    def _decode_components(self) -> tuple[float, float, float, float]:
        return (
            self.t_kernel.decode(self.t),
            self.x_kernel.decode(self.x),
            self.y_kernel.decode(self.y),
            self.z_kernel.decode(self.z),
        )

    def lorentz_boost(self, beta: float, axis: str = "x") -> "FourVector":
        """Return a new four-vector boosted along ``axis``.

        Parameters
        ----------
        beta:
            Normalised velocity (``v/c``) of the boost.
        axis:
            Spatial axis for the boost – ``"x"``, ``"y"`` or ``"z"``.
        """

        if not -1.0 < beta < 1.0:
            raise ValueError("beta must satisfy |beta| < 1")
        gamma = 1.0 / np.sqrt(1 - beta ** 2)
        t, x, y, z = self._decode_components()
        if axis == "x":
            t_new = gamma * (t - beta * x)
            x_new = gamma * (x - beta * t)
            y_new, z_new = y, z
        elif axis == "y":
            t_new = gamma * (t - beta * y)
            y_new = gamma * (y - beta * t)
            x_new, z_new = x, z
        elif axis == "z":
            t_new = gamma * (t - beta * z)
            z_new = gamma * (z - beta * t)
            x_new, y_new = x, y
        else:
            raise ValueError("axis must be 'x', 'y' or 'z'")
        return FourVector(t_new, x_new, y_new, z_new)

    def as_array(self) -> ndarray:
        """Return the decoded ``(t, x, y, z)`` components as an array."""
        return np.array(self._decode_components(), dtype=float)
