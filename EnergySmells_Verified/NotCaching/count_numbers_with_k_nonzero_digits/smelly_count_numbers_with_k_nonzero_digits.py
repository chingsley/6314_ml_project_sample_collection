def count_numbers_with_k_nonzero_digits(N: str, K: int) -> int:
    def rec(digit: int, flag: int, k: int) -> int:
        limit = int(N[digit])

        if k > K:
            return 0

        if digit == len(N) - 1:
            if k == K:
                return 1
            elif k == K - 1:
                return limit if flag else 9
            else:
                return 0

        if flag:
            if limit == 0:
                return rec(digit + 1, 1, k)
            else:
                return (
                    rec(digit + 1, 0, k + 1) * (limit - 1)
                    + rec(digit + 1, 1, k + 1)
                    + rec(digit + 1, 0, k)
                )
        else:
            return rec(digit + 1, 0, k + 1) * 9 + rec(digit + 1, 0, k)

    return rec(0, 1, 0)
