def top_k_recommendations(scores: list, rated_indices: list, k: int) -> list:
    """
    Returns the highest-scoring unrated item indices.
    """
    # Write code here
    for i in rated_indices:
        scores[i]=0
    ans=[]
    while k>0:
        x=scores.index(max(scores))
        ans.append(x)
        scores[x]=0
        k-=1
    return ans
        