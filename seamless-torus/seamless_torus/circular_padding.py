"""Utilities for circular padding."""

import torch
import torch.nn.functional as F


def circular_pad_2d(x: torch.Tensor, pad: int | tuple[int, int, int, int]) -> torch.Tensor:
    """Apply circular padding to an NCHW tensor."""
    if isinstance(pad, int):
        pad = (pad, pad, pad, pad)
    return F.pad(x, pad=pad, mode="circular")
