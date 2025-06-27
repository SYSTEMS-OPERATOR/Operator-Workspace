#!/usr/bin/env python3
"""Simple E8 invariant calculator."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lie_algebra import quadratic_invariant


def parse_representation(values: Sequence[str]) -> np.ndarray:
    """Convert CLI values to a numeric array."""
    try:
        return np.array([float(v) for v in values], dtype=float)
    except ValueError as exc:  # pragma: no cover - arg parsing
        raise argparse.ArgumentTypeError(str(exc)) from exc


def main(argv: Sequence[str] | None = None) -> None:
    """Entry point for the E8 calculator CLI."""
    parser = argparse.ArgumentParser(description="Compute E8 invariant polynomial")
    parser.add_argument("representation", nargs="+", help="vector components")
    args = parser.parse_args(argv)

    vec = parse_representation(args.representation)
    invariant = quadratic_invariant(vec)
    print(invariant)


if __name__ == "__main__":  # pragma: no cover - CLI
    main()
