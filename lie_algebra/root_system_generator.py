"""Generate root systems for simple Lie algebras with caching."""

from __future__ import annotations

from pathlib import Path
import numpy as np

from .lie_algebra import root_system as _root_system


class RootSystemGenerator:
    """Generate root vectors for A, D and E series Lie algebras.

    Parameters
    ----------
    cache_dir:
        Directory where generated root arrays are stored.
    """

    def __init__(self, cache_dir: Path | str = Path("data/roots")) -> None:
        self.cache_dir = Path(cache_dir)

    def roots(self, label: str) -> np.ndarray:
        """Return the root system for ``label``.

        The result is cached under ``cache_dir`` as ``<label>.npy``.
        Supported labels include ``An`` (n>=1), ``Dn`` (n>=4), ``E6``, ``E7``,
        and ``E8``.
        """

        file_path = self.cache_dir / f"{label}.npy"
        if file_path.exists():
            return np.load(file_path)

        if label.startswith("A"):
            rank = int(label[1:])
            roots = self._a_roots(rank)
        elif label.startswith("D"):
            rank = int(label[1:])
            roots = self._d_roots(rank)
        elif label in {"E6", "E7", "E8"}:
            roots = _root_system(label)
        else:
            raise ValueError(f"Unsupported group: {label}")

        file_path.parent.mkdir(parents=True, exist_ok=True)
        np.save(file_path, roots)
        return roots

    @staticmethod
    def _a_roots(n: int) -> np.ndarray:
        m = n + 1
        basis = np.eye(m)
        roots = []
        for i in range(m):
            for j in range(m):
                if i != j:
                    roots.append(basis[i] - basis[j])
        return np.array(roots)

    @staticmethod
    def _d_roots(n: int) -> np.ndarray:
        roots = []
        for i in range(n):
            for j in range(i + 1, n):
                for s1 in (1.0, -1.0):
                    for s2 in (1.0, -1.0):
                        vec = np.zeros(n)
                        vec[i] = s1
                        vec[j] = s2
                        roots.append(vec)
        return np.array(roots)
