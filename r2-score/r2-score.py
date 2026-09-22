import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    """
    Returns the coefficient of determination as a Python float.
    """
    # Write code here
    y_pred=np.asarray(y_pred,dtype=float)
    y_true=np.asarray(y_true,dtype=float)
    mean=np.mean(y_true)
    ans=float(1-(np.sum((y_pred-y_true)**2)/(np.sum((y_true-mean)**2))))
    if np.sum((y_true-mean)**2)==0:
        if (np.sum((y_pred-y_true)**2))==0:
            return 1.0
        else:
            return 0.0
    return ans
    