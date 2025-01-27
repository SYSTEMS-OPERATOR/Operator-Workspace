"""
E3 Data Generator

This module contains the data generator for the E3 group, which is part of the E series data generators.
"""

import numpy as np

class E3DataGenerator:
    """A data generator for the E3 group."""

    def __init__(self, data_size=100):
        """Initialize the data generator with a specified data size."""
        self.data_size = data_size
        self.data = None

    def generate_data(self):
        """Generate data for the E3 group."""
        self.data = np.random.rand(self.data_size, 3)
        return self.data

    def get_data(self):
        """Retrieve the generated data."""
        if self.data is None:
            self.generate_data()
        return self.data
