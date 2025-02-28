def sum_square_differences(n):
    # Sums (i - j)^2 for all 0 <= i, j <= n
    total = 0
    for i in range(n + 1):
        for j in range(n + 1):
            total += (i - j) ** 2
    return total
