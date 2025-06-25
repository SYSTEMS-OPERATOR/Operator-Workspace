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
