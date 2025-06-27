"""E9 Data Generator
This module contains the data generator for the E9 group. It follows the
structure used by the lower E groups."""

import numpy as np

from projects.E8_Model.base_generator import BaseGenerator


class E9DataGenerator(BaseGenerator):
    """A data generator for the E9 group."""

    def __init__(self, data_size: int = 100):
        """Initialize the generator with a specified data size."""
        super().__init__(data_size)

    def generate_data(self):
        """Generate data for the E9 group."""
        # Create a random dataset with nine features
        self.data = np.random.rand(self.data_size, 9)
        return self.data
