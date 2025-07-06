"""Circular padding utilities."""

from __future__ import annotations

import torch
import torch.nn.functional as F


def circular_pad_2d(x: torch.Tensor, pad: int | tuple[int, int, int, int]) -> torch.Tensor:
    """Apply circular (wrap-around) padding to a 4-D tensor (NCHW)."""
    if isinstance(pad, int):
        pad = (pad, pad, pad, pad)
    # F.pad expects (left, right, top, bottom)
    return F.pad(x, pad=pad, mode="circular")
