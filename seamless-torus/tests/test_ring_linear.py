import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import torch
from seamless_torus import RingLinear


def test_ring_forward_consistency():
    layer = RingLinear(8, 8, bias=False)
    x = torch.randn(4, 8)
    y1 = layer(x)
    y2 = layer(x)
    assert y1.shape == y2.shape == (4, 8)
