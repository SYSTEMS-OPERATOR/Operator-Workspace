import abc
from numpy import ndarray
from scipy.linalg import expm, logm


class AbstractBaseKernel(abc.ABC):
    """Base interface for all kernels."""

    @abc.abstractmethod
    def encode(self, q: float | ndarray) -> ndarray:
        """Map physical quantity to Lie-algebra coordinates."""

    @abc.abstractmethod
    def decode(self, v: ndarray) -> float | ndarray:
        """Map Lie-algebra coordinates back to physical quantity."""

    @abc.abstractmethod
    def evolve(self, v: ndarray, tau: float) -> ndarray:
        """Flow under canonical generator by time step ``tau``."""

    @abc.abstractmethod
    def compose(self, *vs: ndarray) -> ndarray:
        """Compose algebra elements with BCH if necessary."""


def bch(a: ndarray, b: ndarray) -> ndarray:
    """Baker-Campbell-Hausdorff using matrix logarithms."""
    return logm(expm(a) @ expm(b)).real
