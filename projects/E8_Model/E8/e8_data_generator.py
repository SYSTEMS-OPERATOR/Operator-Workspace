"""
E8 Data Generator

This module contains the data generator for the E8 group, which is part of the E series data generators.
"""

import numpy as np

class E8DataGenerator:
    """A data generator for the E8 group."""

    def __init__(self, data_size=100):
        """Initialize the data generator with a specified data size."""
        # Store the desired size of the generated dataset
        self.data_size = data_size
        self.data = None

    def generate_data(self):
        """Generate data for the E8 group."""
        # Create a random dataset with eight features
        self.data = np.random.rand(self.data_size, 8)
        return self.data

    def get_data(self):
        """Retrieve the generated data."""
        # Generate data on demand if it does not already exist
        if self.data is None:
            self.generate_data()
        return self.data
