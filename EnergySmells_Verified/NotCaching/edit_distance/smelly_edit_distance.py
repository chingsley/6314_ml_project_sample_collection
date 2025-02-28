def edit_distance(s1, s2):
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    return min(
        edit_distance(s1[1:], s2[1:]) + (0 if s1[0] == s2[0] else 1),
        edit_distance(s1[1:], s2) + 1,
        edit_distance(s1, s2[1:]) + 1,
    )
