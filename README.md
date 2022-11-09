# Overview

A dummy benchmark to validate new feature in #PR

Optimization objective:

$$\min_{x \in \mathbb{R}} \phi(ax + b) \quad \text{, where } a > 0, \ b \in \mathbb{R}$$

with $\phi$ either the identity or $\exp$.

Credits to @mathurinm for the idea.


# Benchmark details:

- Dataset is defined by $(a, b)$
- Solvers minimizes the objective by removing a positive constant from $x$


# Expected behavior

The used solvers subtract a positive constant from $x$.
Hence the objective as a function of ``stop_val=n_iter`` should be a line.
