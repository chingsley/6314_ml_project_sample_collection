def is_prime(num):
    # Checks if num is prime using O(n) divisor checks
    for i in range(2, num):
        if num % i == 0:
            return False
    return num > 1
