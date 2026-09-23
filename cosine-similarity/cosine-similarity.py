import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    x=np.asarray(a,dtype=float)
    y=np.asarray(b,dtype=float)
    if np.sum(x**2)==0 or np.sum(y**2)==0:
        return 0.0
    return float(np.sum(x*y)/(np.sqrt(np.sum(x**2)*np.sum(y**2))))    