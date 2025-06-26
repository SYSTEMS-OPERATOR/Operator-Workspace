from __future__ import annotations

"""Shared base interfaces for the e4d kernels."""

from abc import ABC, abstractmethod
from typing import Iterable

import numpy as np
from numpy import ndarray
from scipy.linalg import expm, logm


class AbstractBaseKernel(ABC):
    """Base interface for all E-series kernels."""

    @abstractmethod
    def encode(self, q: float | ndarray) -> ndarray:
        """Map physical quantity to Lie-algebra coordinates."""

    @abstractmethod
    def decode(self, v: ndarray) -> float | ndarray:
        """Inverse map from Lie coordinates to physical quantity."""

    @abstractmethod
    def evolve(self, v: ndarray, tau: float) -> ndarray:
        """Flow under the canonical generator for time step ``tau``."""

    @abstractmethod
    def compose(self, *vs: ndarray) -> ndarray:
        """Lie-algebra addition with BCH correction when needed."""


# Helpers -------------------------------------------------------------------

def _bch(a: ndarray, b: ndarray) -> ndarray:
    """Compute Baker-Campbell-Hausdorff for matrices using log(exp(a) exp(b))."""
    return logm(expm(a) @ expm(b)).real


