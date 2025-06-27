"""
E4 Data Generator
This module contains the data generator for the E4 group. It is part of the
E series data generators.
"""

import numpy as np

from projects.E8_Model.base_generator import BaseGenerator


class E4DataGenerator(BaseGenerator):
    """A data generator for the E4 group."""

    def __init__(self, data_size: int = 100):
        """Initialize the data generator with a specified data size."""
        super().__init__(data_size)

    def generate_data(self):
        """Generate data for the E4 group."""
        # Create a random dataset with four features
        self.data = np.random.rand(self.data_size, 4)
        return self.data
