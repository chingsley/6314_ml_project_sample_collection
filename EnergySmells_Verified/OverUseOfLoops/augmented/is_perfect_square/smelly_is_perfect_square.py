def is_perfect_square(n):
    # Checks if n is a perfect square via O(n) loop
    for i in range(n + 1):
        if i * i == n:
            return True
    return False
