def count_divisible_pairs(a, b, k):
    # Counts multiples of k using inclusion-exclusion
    multiples_a = a // k
    multiples_b = b // k
    return multiples_a * b + multiples_b * a - multiples_a * multiples_b
