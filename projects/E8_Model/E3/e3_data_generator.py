"""
E3 Data Generator
This module contains the data generator for the E3 group. It is part of the
E series data generators.
"""

import numpy as np

from projects.E8_Model.base_generator import BaseGenerator


class E3DataGenerator(BaseGenerator):
    """A data generator for the E3 group."""

    def __init__(self, data_size: int = 100):
        """Initialize the data generator with a specified data size."""
        super().__init__(data_size)

    def generate_data(self):
        """Generate data for the E3 group."""
        # Create a random dataset with three features
        self.data = np.random.rand(self.data_size, 3)
        return self.data
