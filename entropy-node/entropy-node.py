import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    y=np.asarray(y,dtype=int)
    if len(y)==0:
        return 0.0
    a,x=np.unique(y,return_counts=True)
    probs=x/len(y)
    return -float(np.sum(probs*np.log2(probs)))
    