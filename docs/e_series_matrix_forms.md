# Matrix Forms of the E-Series

This guide lists simple matrix representations for the E-series groups used in
this project. These examples highlight the matrix dimensions and structure of
each group.

## Finite Groups

| Group | Example matrix form | Notes |
|-------|--------------------|-------|
| **E1** | `[λ]` with `λ>0` | scaling by a positive real number |
| **E2** | 2×2 real matrix with determinant 1 | the group `SL(2,ℝ)` |
| **E3** | block `diag(A,B)` with `A∈SL(3,ℝ)`, `B∈SL(2,ℝ)` | sum `SL(3)×SL(2)` |
| **E4** | 5×5 real matrix with determinant 1 | the group `SL(5,ℝ)` |
| **E5** | 10×10 matrix preserving `η=diag(1⁵,-1⁵)` | the split form `SO(5,5)` |
| **E6** | 27×27 real matrix in the fundamental | basic rep of the exceptional group |
| **E7** | 56×56 matrix preserving a symplectic form | fundamental of `E₇` |
| **E8** | 248×248 matrix in the adjoint representation | largest exceptional group |

These matrix sizes reflect common representations used in
supergravity and model building.

## Infinite Extensions

- **E9** is the affine extension `Ē₈`. It has an infinite set of generators that
  can be organised into 248×248 blocks repeated along a loop algebra.
- **E10** is hyperbolic; its generators cannot be captured by finite matrices and
  grow without bound along a Lorentzian lattice.
- **E11** is the very extended algebra. It similarly requires infinitely many
  generators and is usually described abstractly rather than by matrices.

The infinite algebras motivate hierarchical structures in matrix models but do
not admit fixed-size matrix representations.
