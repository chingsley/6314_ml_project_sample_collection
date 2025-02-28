def find_matching_pairs(s):
    # Finds pairs of identical characters separated by 1 position
    pairs = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if j == i + 1 and s[i] == s[j]:
                pairs.append((i, j))
    return pairs
