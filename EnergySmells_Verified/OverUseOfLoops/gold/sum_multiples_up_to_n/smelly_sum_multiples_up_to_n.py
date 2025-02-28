def sum_multiples_up_to_n(n):
    ans = 0

    for i in range(1, n + 1):
        k = n // i
        ans += k * (k + 1) // 2 * i

    return ans
