"""Tests for E-group data generators."""

import unittest

from projects.E8_Model.E1.e1_data_generator import E1DataGenerator
from projects.E8_Model.E2.e2_data_generator import E2DataGenerator
from projects.E8_Model.E3.e3_data_generator import E3DataGenerator
from projects.E8_Model.E4.e4_data_generator import E4DataGenerator
from projects.E8_Model.E5.e5_data_generator import E5DataGenerator
from projects.E8_Model.E6.e6_data_generator import E6DataGenerator
from projects.E8_Model.E7.e7_data_generator import E7DataGenerator
from projects.E8_Model.E8.e8_data_generator import E8DataGenerator


class TestGenerators(unittest.TestCase):
    def _check_generator(self, generator_cls, expected_dim):
        generator = generator_cls(data_size=3)
        data = generator.get_data()
        self.assertEqual(data.shape, (3, expected_dim))

    def test_e1(self):
        self._check_generator(E1DataGenerator, 1)

    def test_e2(self):
        self._check_generator(E2DataGenerator, 2)

    def test_e3(self):
        self._check_generator(E3DataGenerator, 3)

    def test_e4(self):
        self._check_generator(E4DataGenerator, 4)

    def test_e5(self):
        self._check_generator(E5DataGenerator, 5)

    def test_e6(self):
        self._check_generator(E6DataGenerator, 6)

    def test_e7(self):
        self._check_generator(E7DataGenerator, 7)

    def test_e8(self):
        self._check_generator(E8DataGenerator, 8)


if __name__ == "__main__":
    unittest.main()
