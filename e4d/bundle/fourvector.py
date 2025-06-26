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
        else:
            t_new = gamma * (t - beta * z)
            z_new = gamma * (z - beta * t)
            x_new, y_new = x, y
        return FourVector(t_new, x_new, y_new, z_new)

    def as_array(self) -> ndarray:
        flat = [self.t, self.x.flatten(), self.y.flatten(), self.z.flatten()]
        return np.hstack(flat)
