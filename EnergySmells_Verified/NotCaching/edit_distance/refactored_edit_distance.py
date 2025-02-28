def edit_distance(s1, s2, memo=None):
    if memo is None:
        memo = {}
    if (s1, s2) in memo:
        return memo[(s1, s2)]
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    cost = 0 if s1[0] == s2[0] else 1
    result = min(
        edit_distance(s1[1:], s2[1:], memo) + cost,
        edit_distance(s1[1:], s2, memo) + 1,
        edit_distance(s1, s2[1:], memo) + 1,
    )
    memo[(s1, s2)] = result
    return result
