import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    sigmoid = lambda x : 1 / (1 + np.exp(-x))
    fun = np.vectorize(sigmoid)
    x = fun(x)
    return x