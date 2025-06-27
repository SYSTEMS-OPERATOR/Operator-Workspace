"""
E6 Data Generator
This module contains the data generator for the E6 group. It is part of the
E series data generators.
"""

import numpy as np

from lie_algebra import root_system
from projects.E8_Model.base_generator import BaseGenerator


class E6DataGenerator(BaseGenerator):
    """A data generator for the E6 group."""

    def __init__(self, data_size: int = 100):
        super().__init__(data_size)

    def generate_data(self):
        """Generate data for the E6 group."""
        roots = root_system("E6")[:, :6]
        reps = roots[: self.data_size]
        self.data = np.array(reps, dtype=float)
        return self.data
