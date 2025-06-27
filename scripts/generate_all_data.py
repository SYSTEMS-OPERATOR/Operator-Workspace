"""Generate sample data for all E-group data generators."""

from pathlib import Path
import sys
import argparse

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
from projects.E8_Model.E9.e9_data_generator import E9DataGenerator
from projects.E8_Model.E10.e10_data_generator import E10DataGenerator
from projects.E8_Model.E11.e11_data_generator import E11DataGenerator


GENERATOR_MAP = {
    "E1": E1DataGenerator,
    "E2": E2DataGenerator,
    "E3": E3DataGenerator,
    "E4": E4DataGenerator,
    "E5": E5DataGenerator,
    "E6": E6DataGenerator,
    "E7": E7DataGenerator,
    "E8": E8DataGenerator,
    "E9": E9DataGenerator,
    "E10": E10DataGenerator,
    "E11": E11DataGenerator,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate E-group datasets")
    parser.add_argument("--group", default="E8", help="group label, e.g. E8")
    parser.add_argument("--size", type=int, default=5, help="dataset size")
    parser.add_argument("--format", choices=["csv", "json", "npz"], default="json")
    parser.add_argument("--out", type=Path, default=Path("data.json"), help="output file")
    args = parser.parse_args()

    gen_cls = GENERATOR_MAP.get(args.group)
    if gen_cls is None:
        raise SystemExit(f"Unknown group: {args.group}")
    generator = gen_cls(data_size=args.size)
    if args.format == "csv":
        generator.export_csv(args.out)
    elif args.format == "json":
        generator.export_json(args.out)
    else:
        generator.export_npz(args.out)
    print(f"Saved {args.group} data to {args.out}")


if __name__ == "__main__":
    main()
