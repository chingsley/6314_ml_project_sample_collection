def check_subset_sum_exists(A: list, queries: list) -> list:
    r = set()

    def f(s, k):
        if k >= 0:
            r.add(s)
            f(s + A[k - 1], k - 1)
            f(s, k - 1)

    f(0, len(A))
    return ["yes" if e in r else "no" for e in queries]
