import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import torch
from seamless_torus import circular_pad_2d


def test_circular_shape():
    x = torch.randn(2, 3, 4, 4)
    y = circular_pad_2d(x, 1)
    assert y.shape == (2, 3, 6, 6)
