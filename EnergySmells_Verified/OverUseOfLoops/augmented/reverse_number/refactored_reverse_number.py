def reverse_number(n):
    # Reverses digits mathematically in O(log n) time
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num
