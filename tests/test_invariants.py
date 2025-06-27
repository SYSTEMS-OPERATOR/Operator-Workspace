import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from projects.lie_algebra import cartan_matrix, root_system, weyl_group_order


class TestInvariants(unittest.TestCase):
    def test_e8_invariants(self):
        self.assertEqual(len(root_system("E8")), 240)
        self.assertEqual(cartan_matrix("E8").shape, (8, 8))
        self.assertEqual(weyl_group_order("E8"), 696729600)


if __name__ == "__main__":
    unittest.main()
