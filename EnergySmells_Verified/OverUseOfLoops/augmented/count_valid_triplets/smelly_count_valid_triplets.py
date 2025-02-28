def count_divisible_pairs(a, b, k):
    # Counts pairs (x, y) where x <= a, y <= b, and x*y % k == 0
    count = 0
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            if (x * y) % k == 0:
                count += 1
    return count
