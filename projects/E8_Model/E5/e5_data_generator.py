"""
E5 Data Generator
This module contains the data generator for the E5 group. It is part of the
E series data generators.
"""

import numpy as np

from projects.E8_Model.base_generator import BaseGenerator


class E5DataGenerator(BaseGenerator):
    """A data generator for the E5 group."""

    def __init__(self, data_size: int = 100):
        """Initialize the data generator with a specified data size."""
        super().__init__(data_size)

    def generate_data(self):
        """Generate data for the E5 group."""
        # Create a random dataset with five features
        self.data = np.random.rand(self.data_size, 5)
        return self.data
