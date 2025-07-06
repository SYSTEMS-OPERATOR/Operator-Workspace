"""RingLinear module implementing toroidal weight wrapping."""

from __future__ import annotations

import math
import torch
from torch import nn


class RingLinear(nn.Module):
    """Fully connected layer with toroidal weight wrapping."""

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

    def roll(self, tensor: torch.Tensor, shift: int, dim: int) -> torch.Tensor:
        """Roll tensor in the given dimension."""
        if shift == 0:
            return tensor
        dim_size = tensor.size(dim)
        shift = shift % dim_size
        head = tensor.narrow(dim, dim_size - shift, shift)
        tail = tensor.narrow(dim, 0, dim_size - shift)
        return torch.cat((head, tail), dim=dim)

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        """Compute forward pass with rolled weight."""
        if input.ndim != 2 or input.size(1) != self.in_features:
            raise ValueError("Input must be of shape (batch, in_features)")
        bshift = input.shape[0] % self.in_features
        weight_roll = self.roll(self.weight, bshift, dim=1)
        output = input @ weight_roll.T
        if self.bias is not None:
            output = output + self.bias
        return output
