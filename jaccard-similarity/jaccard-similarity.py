def jaccard_similarity(set_a: list, set_b: list) -> float:
    """
    Returns the Jaccard similarity of the two item collections.
    """
    # Write code here
    na,nb=len(set_a),len(set_b)
    a=set(set_a)
    b=set(set_b)
    if not(na and nb):
        return 0.0
    return float(len(a&b)/len(a|b))