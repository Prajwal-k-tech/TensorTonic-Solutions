# TensorTonic Solutions

A small machine-learning practice archive synchronized from [TensorTonic](https://www.tensortonic.com). It currently contains dot product, cosine similarity and sigmoid exercises. This is supporting study work rather than a research project or general ML library.

## Current implementation notes

- Dot product currently calls `numpy.dot`; it is not a manual multiply-and-sum implementation, despite the synchronized problem description below.
- Cosine similarity uses NumPy dot products and norms and returns zero when either norm is zero.
- Sigmoid uses `numpy.vectorize` around the direct exponential formula. Large negative inputs can overflow internally; scalar-return and empty-array behavior require improvement before claiming complete edge-case coverage.

The generated platform section below is retained for synchronization. Its verification badge reflects the platform record, not an independent audit of every edge case or a claim about repository-wide quality. Each exercise folder contains code and accompanying notes. Install NumPy in a virtual environment to explore the snippets; no package or test suite is configured.

<!-- tensortonic:start -->
# Prajwal K's TensorTonic Solutions

Verified machine learning implementations completed on [TensorTonic](https://www.tensortonic.com).

<p align="center">
  <img src="https://www.tensortonic.com/api/badge/prajwal_k141205.svg" alt="TensorTonic Verified Solutions" width="100%" />
</p>

| Problem | Description | Link |
|---|---|---|
| Implement Cosine Similarity | Compute cosine similarity between NumPy vectors with dot products, Euclidean norms, and zero-vector handling. | https://www.tensortonic.com/problems/cosine-similarity |
| Implement Dot Product | Implement the dot product of equal-length numeric vectors by summing element-wise products without library shortcuts. | https://www.tensortonic.com/problems/dot-product |
| Implement Sigmoid in NumPy | Implement a vectorized sigmoid activation in NumPy for scalars, lists, vectors, and matrices, including large positive and negative inputs. | https://www.tensortonic.com/problems/sigmoid-numpy |

View my verified ML profile: [TensorTonic profile](https://www.tensortonic.com/profile/prajwal_k141205)
<!-- tensortonic:end -->
