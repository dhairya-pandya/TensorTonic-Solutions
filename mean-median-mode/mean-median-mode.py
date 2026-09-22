from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    hmap={}
    x=np.asarray(x,dtype=float)
    hmap["mean"]=float(np.mean(x))
    hmap["median"]=float(np.median(x))
    c=Counter(x)
    mode=x[0]
    f=1
    for i in range(len(x)):
        if c[x[i]]>f:
            mode=x[i]
            f=c[x[i]]
    hmap["mode"]=float(mode)
    return hmap