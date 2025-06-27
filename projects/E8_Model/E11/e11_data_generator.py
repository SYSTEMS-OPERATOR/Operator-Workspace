"""E11 Data Generator
This module contains the data generator for the E11 group."""

import numpy as np

from projects.E8_Model.base_generator import BaseGenerator


class E11DataGenerator(BaseGenerator):
    """A data generator for the E11 group."""

    def __init__(self, data_size: int = 100):
        """Initialize the generator with a specified data size."""
        super().__init__(data_size)

    def generate_data(self):
        """Generate data for the E11 group."""
        # Create a random dataset with eleven features
        self.data = np.random.rand(self.data_size, 11)
        return self.data
