# Matrix Forms of the E-Series

This note summarises simple matrix representations for the groups E1–E11. These
expressions are schematic: only the low-rank classical groups have obvious
matrix realisations. The larger exceptional groups require more elaborate
constructions, but we indicate their typical dimensions for reference.

## Finite groups E1–E8

| Group | Typical matrix realisation | Example dimension |
|-------|----------------------------|------------------:|
| **E1** | scalar rescaling $r \in \mathbb{R}^+$ | $1\times1$ |
| **E2** | $2\times2$ traceless matrices ($\mathfrak{sl}(2)$) | $2\times2$ |
| **E3** | block $\mathfrak{sl}(3)\oplus\mathfrak{sl}(2)$ | $3\times3$ and $2\times2$ |
| **E4** | traceless $5\times5$ matrices ($\mathfrak{sl}(5)$) | $5\times5$ |
| **E5** | antisymmetric $10\times10$ matrices ($\mathfrak{so}(10)$) | $10\times10$ |
| **E6** | fundamental rep. on $\mathbb{C}^{27}$ | $27\times27$ |
| **E7** | acts on the $56$ of supergravity | $56\times56$ |
| **E8** | adjoint action in $\mathbb{C}^{248}$ | $248\times248$ |

## Infinite extensions E9–E11

These are Kac–Moody algebras with infinitely many generators. Finite-dimensional
matrix forms do not exist, but their low-level generators mirror those of E8.

| Group | Notes |
|-------|------|
| **E9** | affine extension of E8; currents in 2D supergravity |
| **E10** | hyperbolic algebra controlling cosmological billiards |
| **E11** | very-extended algebra conjectured in M-theory |

For practical calculations one often truncates to the finite sectors matching
supergravity fields. Detailed constructions can be found in the references
listed in `exceptional_lie_groups.md`.

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

