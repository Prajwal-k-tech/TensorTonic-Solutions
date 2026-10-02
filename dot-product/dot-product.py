def dot_product(x: list, y: list) -> float:
    """Return the dot product of equal-length numeric vectors."""
    if len(x) != len(y):
        raise ValueError("Vectors must have equal lengths")
    return float(sum(a * b for a, b in zip(x, y)))
