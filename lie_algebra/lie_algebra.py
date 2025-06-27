"""Basic utilities for exceptional Lie algebras."""

from __future__ import annotations

import itertools
import numpy as np

from .constants import E6_CARTAN, E7_CARTAN, E8_CARTAN, WEYL_ORDERS


def cartan_matrix(group: str) -> np.ndarray:
    """Return the Cartan matrix for a given exceptional group."""
    if group == "E6":
        return E6_CARTAN
    if group == "E7":
        return E7_CARTAN
    if group == "E8":
        return E8_CARTAN
    raise ValueError(f"Unsupported group: {group}")


def root_system(group: str) -> np.ndarray:
    """Generate the root system for ``group``."""
    roots = []
    # build full E8 roots
    for i in range(8):
        for j in range(i + 1, 8):
            for s1 in [1, -1]:
                for s2 in [1, -1]:
                    v = [0.0] * 8
                    v[i] = float(s1)
                    v[j] = float(s2)
                    roots.append(v)
    for signs in itertools.product([1, -1], repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append([0.5 * s for s in signs])
    if group == "E8":
        return np.array(roots)
    roots = [v for v in roots if abs(sum(v)) < 1e-12]
    if group == "E7":
        return np.array(roots)
    if group == "E6":
        roots = [v for v in roots if abs(v[6] + v[7]) < 1e-12]
        return np.array(roots)
    raise ValueError(f"Unsupported group: {group}")


def weyl_group_order(group: str) -> int:
    """Return the Weyl group order."""
    try:
        return WEYL_ORDERS[group]
    except KeyError as exc:
        raise ValueError(f"Unsupported group: {group}") from exc
