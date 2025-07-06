"""Fully connected layer with toroidal weight matrix."""

from __future__ import annotations

import math
from typing import Optional

import torch
from torch import nn


class RingLinear(nn.Module):
    """Linear layer whose weight matrix is rolled on each forward pass."""

    in_features: int
    out_features: int
    bias: Optional[nn.Parameter]

    def __init__(self, in_features: int, out_features: int, bias: bool = True) -> None:
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.weight = nn.Parameter(torch.empty(out_features, in_features))
        if bias:
            self.bias = nn.Parameter(torch.empty(out_features))
        else:
            self.register_parameter("bias", None)
        self.reset_parameters()

    def reset_parameters(self) -> None:
        nn.init.kaiming_uniform_(self.weight, a=math.sqrt(5))
        if self.bias is not None:
            fan_in, _ = nn.init._calculate_fan_in_and_fan_out(self.weight)
            bound = 1 / math.sqrt(fan_in)
            nn.init.uniform_(self.bias, -bound, bound)

    @staticmethod
    def _roll(tensor: torch.Tensor, shift: int, dim: int) -> torch.Tensor:
        """Roll tensor along dimension using circular shift."""
        if tensor.size(dim) == 0:
            return tensor
        shift = shift % tensor.size(dim)
        if shift == 0:
            return tensor
        return torch.cat(
            (tensor.narrow(dim, tensor.size(dim) - shift, shift),
             tensor.narrow(dim, 0, tensor.size(dim) - shift)),
            dim=dim,
        )

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        bshift = int(input.shape[0] % self.in_features)
        weight_roll = self._roll(self.weight, bshift, dim=1)
        output = input.matmul(weight_roll.T)
        if self.bias is not None:
            output = output + self.bias
        return output
