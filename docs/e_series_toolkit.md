# E-Series Research Toolkit

This document provides a compact reference for the exceptional groups E6--E8 and their infinite extensions E9--E11. It consolidates key dimensions, ranks, root counts, and literature pointers for further study.

## Quick Reference Tables

| Label | Algebra | Rank | Dim | # roots | Key invariants | Canonical real form in SUGRA |
|------|---------|-----:|----:|-------:|----------------|------------------------------|
| **E8** | \(\mathfrak{e}_8\) | 8 | 248 | 240 | degree-8 scalar | 3D, \(E_{8(8)}\) U-duality |
| **E7** | \(\mathfrak{e}_7\) | 7 | 133 | 126 | quartic | 4D, \(E_{7(7)}\) |
| **E6** | \(\mathfrak{e}_6\) | 6 | 78 | 72 | cubic | 5D, \(E_{6(6)}\) |
| **E5** | \(\mathfrak{so}(10)\) | 5 | 45 | 40 | Pfaffian | 6D, \(SO(5,5)\) |
| **E4** | \(\mathfrak{sl}(5)\) | 4 | 24 | 20 | det | 7D, \(SL(5)\) |
| **E3** | \(\mathfrak{sl}(3)\oplus\mathfrak{sl}(2)\) | 3 | 11 | 8 | -- | 8D, \(SL(3)\times SL(2)\) |
| **E2** | \(\mathfrak{sl}(2)\) | 1 | 3 | 2 | -- | 9D, \(SL(2)\times\mathbb{R}^+\) |
| **E1** | \(\mathbb{R}^+\) | 1 | 1 | -- | -- | 10D dilaton scale |

For the Kac--Moody extensions:

| Label | Type | Rank | Status in M-theory | Primary references |
|------|------|-----:|--------------------|-------------------|
| **E9** | affine \(\widehat{E}_8\) | 9 | symmetry in 2D maximal SUGRA | Bossard et al. (2021) |
| **E10** | hyperbolic | 10 | near-singularity cosmological billiards | Damour--Henneaux--Nicolai (2002) |
| **E11** | very-extended | 11 | conjectured master symmetry | West (2001 ff.) |

## Literature Stack

- Humphreys, *Introduction to Lie Algebras & Representation Theory*.
- Fuchs & Schweigert, *Symmetries, Lie Algebras and Representations*.
- Obers & Pioline, *U-Duality and M-Theory*.
- Damour, Henneaux & Nicolai, *Cosmological Billiards*.
- Bossard et al., *E9 Exceptional Field Theory*.
- West, *E11 and M Theory*.

## Computational Tools

Use SageMath or LiE to confirm ranks, dimensions and branching rules. Example:

```python
from sage.all import RootSystem
roots = RootSystem(['E', 8]).root_lattice().roots()
```

This snippet lists all 240 E8 roots, providing a quick sanity check for table entries.

## Physical Context

1. **U-duality chain**: Compactifying 11D supergravity on \(T^d\) reveals \(E_{11-d}\) symmetries.
2. **Gauge enhancement**: The heterotic string realizes \(E_8\times E_8\) gauge groups.
3. **Black-hole invariants**: The E7 quartic invariant encodes 4D extremal entropy.
4. **Cosmological billiards**: E10 describes chaotic trajectories near singularities.
5. **E9/EFT**: Two-dimensional reductions gain an affine current algebra.
6. **E11 conjecture**: West's non-linear realisation suggests a unifying symmetry.

## Suggested Learning Path

1. **Classical Lie theory**: derive Dynkin diagrams and Cartan matrices with Sage.
2. **Exceptional invariants**: reproduce the E6 cubic and E7 quartic forms.
3. **Supergravity dualities**: study how \(E_{7(7)}(\mathbb{Z})\) acts on charge vectors.
4. **Kac--Moody & EFT**: implement level decompositions of E9 and E10.

