def gcd(a, b):
    # Uses Euclidean algorithm (O(log n) time)
    while b:
        a, b = b, a % b
    return a
