"""Tests for RingLinear layer."""

import torch
from seamless_torus import RingLinear


def test_ring_forward_consistency() -> None:
    layer = RingLinear(8, 8, bias=False)
    x = torch.randn(4, 8)
    y1 = layer(x)
    y2 = layer(x)
    assert y1.shape == y2.shape == (4, 8)
