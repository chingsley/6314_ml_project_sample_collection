def sum_of_squares(n):
    # Computes sum of squares of numbers from 1 to n
    total = 0
    for i in range(1, n + 1):
        total += i**2
    return total
