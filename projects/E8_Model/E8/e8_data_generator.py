"""
E8 Data Generator

This module contains the data generator for the E8 group. It is part of the
E series data generators.
"""

import numpy as np

from ...lie_algebra import root_system


class E8DataGenerator:
    """A data generator for the E8 group."""

    def __init__(self, data_size=100):
        """Initialize the data generator with a specified data size."""
        # Store the desired size of the generated dataset
        self.data_size = data_size
        self.data = None

    def generate_data(self):
        """Generate data for the E8 group using its root system."""
        roots = root_system("E8")
        idx = np.random.choice(len(roots), self.data_size, replace=True)
        self.data = roots[idx]
        return self.data

    def get_data(self):
        """Retrieve the generated data."""
        # Generate data on demand if it does not already exist
        if self.data is None:
            self.generate_data()
        return self.data

    def export_data(self, path, fmt="csv"):
        """Export generated data to ``path`` in the given format."""
        data = self.get_data()
        if fmt == "csv":
            np.savetxt(path, data, delimiter=",")
        elif fmt == "json":
            import json

            with open(path, "w", encoding="utf-8") as fh:
                json.dump(data.tolist(), fh)
        elif fmt == "npz":
            np.savez(path, data=data)
        else:
            raise ValueError(f"Unknown format: {fmt}")
