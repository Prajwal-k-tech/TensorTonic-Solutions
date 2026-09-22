import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    numerator = np.dot(a,b);
    deno = np.linalg.norm(a) * np.linalg.norm(b)
    if(deno == 0):
        return 0.0
    else :
        return float(numerator/deno);
    