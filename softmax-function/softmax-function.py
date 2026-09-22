import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    if  len(np.shape(x))==1:
        mx=np.max(x)
        x=x-mx
        d=np.sum(np.exp(x))
        return np.array(np.exp(x)/d)
    else:
        mx=np.max(x,axis=1,keepdims=True)
        x=x-mx
        d=np.sum(np.exp(x),axis=1,keepdims=True)
        return np.array(np.exp(x)/d)