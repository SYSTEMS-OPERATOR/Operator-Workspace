"""Generate sample data for all E-group data generators."""

from pathlib import Path
import sys

# Ensure the repository root is on the Python path so the ``projects`` package
# imports correctly when this script is executed directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from projects.E8_Model.E1.e1_data_generator import E1DataGenerator
from projects.E8_Model.E2.e2_data_generator import E2DataGenerator
from projects.E8_Model.E3.e3_data_generator import E3DataGenerator
from projects.E8_Model.E4.e4_data_generator import E4DataGenerator
from projects.E8_Model.E5.e5_data_generator import E5DataGenerator
from projects.E8_Model.E6.e6_data_generator import E6DataGenerator
from projects.E8_Model.E7.e7_data_generator import E7DataGenerator
from projects.E8_Model.E8.e8_data_generator import E8DataGenerator


GENERATORS = [
    ("E1", E1DataGenerator),
    ("E2", E2DataGenerator),
    ("E3", E3DataGenerator),
    ("E4", E4DataGenerator),
    ("E5", E5DataGenerator),
    ("E6", E6DataGenerator),
    ("E7", E7DataGenerator),
    ("E8", E8DataGenerator),
]


def main():
    for name, generator_cls in GENERATORS:
        generator = generator_cls(data_size=5)
        data = generator.get_data()
        print(f"{name}: {data.shape}")


if __name__ == "__main__":
    main()
