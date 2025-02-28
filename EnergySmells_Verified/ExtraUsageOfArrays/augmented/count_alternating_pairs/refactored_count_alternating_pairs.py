def count_alternating_pairs(s):
    return min(
        s.count("0"), s.count("1")
    )  # Same logic as smelly code but more efficient!
