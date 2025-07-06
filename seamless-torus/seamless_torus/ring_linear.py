"""RingLinear module implementing toroidal fully-connected layer."""
from __future__ import annotations

import math
import torch
from torch import nn


class RingLinear(nn.Module):
    """Linear layer whose weight matrix behaves like a 2-D torus."""

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
    def roll(tensor: torch.Tensor, shift: int, dim: int) -> torch.Tensor:
        """Roll a tensor along a dimension without wrap artefacts."""
        part1 = tensor.narrow(dim, -shift, shift)
        part2 = tensor.narrow(dim, 0, tensor.size(dim) - shift)
        return torch.cat((part1, part2), dim=dim)

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        """Apply the ring-linear transform."""
        shift = int(input.shape[0] % self.in_features)
        weight_roll = self.roll(self.weight, shift, dim=1)
        output = torch.matmul(input, weight_roll.T)
        if self.bias is not None:
            output += self.bias
        return output
