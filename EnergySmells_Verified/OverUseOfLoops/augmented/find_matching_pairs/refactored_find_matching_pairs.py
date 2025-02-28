def find_matching_pairs(s):
    # Uses a single loop with early termination
    return [(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
