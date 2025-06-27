"""Common utilities for E-series data generators."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


class BaseGenerator:
    """Base generator with export helpers."""

    def __init__(self, data_size: int = 100):
        self.data_size = data_size
        self.data: np.ndarray | None = None

    def get_data(self) -> np.ndarray:
        if self.data is None:
            self.generate_data()
        return self.data

    def export_csv(self, path: Path) -> Path:
        np.savetxt(path, self.get_data(), delimiter=",")
        return path

    def export_json(self, path: Path) -> Path:
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(self.get_data().tolist(), fh)
        return path

    def export_npz(self, path: Path) -> Path:
        np.savez(path, data=self.get_data())
        return path

    def generate_data(self) -> None:  # pragma: no cover - to override
        raise NotImplementedError
