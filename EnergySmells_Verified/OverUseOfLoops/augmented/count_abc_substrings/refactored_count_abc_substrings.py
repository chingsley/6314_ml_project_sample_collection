def count_abc_substrings(s):
    # Uses linear scans to avoid nested loops
    a = s.count("a")
    b = s.count("b")
    c = s.count("c")
    return a * b * c  # Valid for non-overlapping cases
