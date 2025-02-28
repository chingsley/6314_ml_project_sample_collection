def gcd(a, b):
    # Computes GCD using O(min(a,b)) iterations
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
