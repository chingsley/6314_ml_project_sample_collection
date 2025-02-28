def check_subset_sum_exists(A: list, queries: list) -> list:
    s = {0}
    for a in A:
        for b in list(s):
            s.add(a + b)
    return ["yes" if e in s else "no" for e in queries]
