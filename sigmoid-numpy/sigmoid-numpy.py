import numpy as np


def sigmoid(x: list | float) -> np.ndarray | float:
    """Compute sigmoid without exponential overflow, preserving input shape."""
    values = np.asarray(x, dtype=float)
    result = np.empty_like(values)
    positive = values >= 0
    result[positive] = 1.0 / (1.0 + np.exp(-values[positive]))
    exp_values = np.exp(values[~positive])
    result[~positive] = exp_values / (1.0 + exp_values)
    return float(result) if result.ndim == 0 else result
