def count_factors(num):
    # Counts factors up to sqrt(num)
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 1 if i == num // i else 2
    return count
