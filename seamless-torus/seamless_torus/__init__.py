"""Seamless-Torus — toroidal layers & utilities for boundary-free neural nets."""

from .circular_padding import circular_pad_2d
from .ring_linear import RingLinear

__all__ = ["circular_pad_2d", "RingLinear"]
