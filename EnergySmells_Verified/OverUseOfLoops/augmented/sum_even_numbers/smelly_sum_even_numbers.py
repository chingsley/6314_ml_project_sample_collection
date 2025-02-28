def sum_even_numbers(n):
    # Sums even numbers from 1 to n using a loop
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total
