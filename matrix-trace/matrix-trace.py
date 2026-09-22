import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    trace=0
    m,n=len(A),len(A[0])
    for i in range(m):
        for j in range(n):
            if i==j:
                trace+=A[i][j]
    return trace