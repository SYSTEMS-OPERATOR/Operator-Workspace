"""Invariant polynomial utilities for exceptional groups."""

from __future__ import annotations

import numpy as np
from numpy import ndarray


def quadratic_invariant(vec: ndarray) -> float:
    """Return the quadratic invariant ``x^2`` for ``vec``."""
    vec = np.asarray(vec, dtype=float)
    return float(np.dot(vec, vec))
