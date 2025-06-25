"""Tests for E-group data generators."""

import sys
from pathlib import Path
import unittest

# Ensure local 'projects' package is used
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from projects.E8_Model.E1.e1_data_generator import E1DataGenerator
from projects.E8_Model.E2.e2_data_generator import E2DataGenerator
from projects.E8_Model.E3.e3_data_generator import E3DataGenerator
from projects.E8_Model.E4.e4_data_generator import E4DataGenerator
from projects.E8_Model.E5.e5_data_generator import E5DataGenerator
from projects.E8_Model.E6.e6_data_generator import E6DataGenerator
from projects.E8_Model.E7.e7_data_generator import E7DataGenerator
from projects.E8_Model.E8.e8_data_generator import E8DataGenerator
from projects.E8_Model.E9.e9_data_generator import E9DataGenerator
from projects.E8_Model.E10.e10_data_generator import E10DataGenerator
from projects.E8_Model.E11.e11_data_generator import E11DataGenerator


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

    def test_e9(self):
        self._check_generator(E9DataGenerator, 9)

    def test_e10(self):
        self._check_generator(E10DataGenerator, 10)

    def test_e11(self):
        self._check_generator(E11DataGenerator, 11)


if __name__ == "__main__":
    unittest.main()
