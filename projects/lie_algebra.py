"""Utility functions for exceptional Lie algebras."""

from __future__ import annotations

import numpy as np
from sympy.liealgebras.cartan_matrix import CartanMatrix
from sympy.liealgebras.root_system import RootSystem
from sympy.liealgebras.weyl_group import WeylGroup

from .constants import WEYL_GROUP_ORDER


def cartan_matrix(group: str) -> np.ndarray:
    """Return the Cartan matrix for an exceptional group."""
    return np.array(CartanMatrix(group), dtype=int)


def root_system(group: str) -> np.ndarray:
    """Return the simple root system as an array."""
    rs = RootSystem(group).all_roots()
    root_vecs = np.array([rs[i] for i in sorted(rs)], dtype=int)
    if group.startswith("E"):
        rank = int(group[1:])
        if rank < root_vecs.shape[1]:
            root_vecs = root_vecs[:, :rank]
    return root_vecs


def weyl_group_order(group: str) -> int:
    """Return the Weyl group order for ``group``."""
    if group in WEYL_GROUP_ORDER:
        return WEYL_GROUP_ORDER[group]
    return WeylGroup(group).group_order()
