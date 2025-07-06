# Seamless-Torus 🌀

Toroidal padding & RingLinear layers that eliminate boundary artifacts and
round-off drift in neural-network pipelines. Built in the `operator-workspace`
monorepo.

## Install (from source)

```bash
git clone https://github.com/<ORG>/operator-workspace.git
cd operator-workspace/seamless-torus
pip install -e .[dev]
```

## Quick start

```python
import torch
from seamless_torus import circular_pad_2d, RingLinear

x = torch.randn(1, 3, 32, 32)
y = circular_pad_2d(x, 2)
print(y.shape)  # (1, 3, 36, 36)

mlp = RingLinear(128, 128)
out = mlp(torch.randn(10, 128))
```

## Citation

If you use this package, please cite the companion paper
*“Seamless Neural-Network Optimization: From Circular Padding to Toroidal
Transformers”* (preprint 2025).
