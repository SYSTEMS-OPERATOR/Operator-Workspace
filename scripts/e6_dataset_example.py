"""Example dataset generation for the E6 algebra module.

This script demonstrates how to create a toy dataset for training the
E6 module. It uses :class:`~projects.E8_Model.E6.e6_data_generator.E6DataGenerator`
to generate random samples and saves them to a ``.npy`` file.

Run this file directly to produce ``e6_dataset.npy`` in the current
directory. The dataset has 10 samples with six features each.
"""

from pathlib import Path
import numpy as np

from projects.E8_Model.E6.e6_data_generator import E6DataGenerator


DEFAULT_OUTPUT = Path("e6_dataset.npy")


def build_dataset(output_path: Path = DEFAULT_OUTPUT) -> Path:
    """Generate and store a toy E6 dataset.

    Parameters
    ----------
    output_path:
        Destination for the ``.npy`` file.

    Returns
    -------
    Path
        The path to the saved dataset file.
    """
    generator = E6DataGenerator(data_size=10)
    data = generator.get_data()
    np.save(output_path, data)
    print(f"Saved dataset with shape {data.shape} to {output_path}")
    return output_path


def main() -> None:
    """Entry point for the example script."""
    build_dataset()


if __name__ == "__main__":
    main()
