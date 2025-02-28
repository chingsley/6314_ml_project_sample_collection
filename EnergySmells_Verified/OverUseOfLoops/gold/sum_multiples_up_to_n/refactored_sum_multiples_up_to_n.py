def sum_multiples_up_to_n(n):
    ans = 0
    lastk = n
    for i in range(1, n + 1):
        k = n // i
        ans += i * (i - 1) // 2 * (lastk + k + 1) * (lastk - k) // 2
        if i > k:
            break

        ans += k * (k + 1) // 2 * i
        if i == k:
            break

        lastk = k

    return ans
