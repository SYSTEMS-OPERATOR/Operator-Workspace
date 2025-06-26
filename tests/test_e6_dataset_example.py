import numpy as np
from pathlib import Path

from scripts.e6_dataset_example import build_dataset


def test_e6_dataset_example(tmp_path: Path) -> None:
    output_file = tmp_path / "sample.npy"
    result_path = build_dataset(output_file)
    assert result_path == output_file
    data = np.load(output_file)
    assert data.shape == (10, 6)
