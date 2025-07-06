"""Tests for circular padding."""

import torch
from seamless_torus import circular_pad_2d


def test_circular_shape() -> None:
    x = torch.randn(2, 3, 4, 4)
    y = circular_pad_2d(x, 1)
    assert y.shape == (2, 3, 6, 6)
