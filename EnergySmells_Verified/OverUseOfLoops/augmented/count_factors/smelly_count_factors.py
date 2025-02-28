def count_factors(num):
    # Counts factors of num using O(n) checks
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count
