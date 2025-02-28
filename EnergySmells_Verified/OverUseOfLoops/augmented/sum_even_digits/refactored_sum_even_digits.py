def sum_even_digits(s):
    # Sums even digits using nested loops
    total = 0
    digits = []
    for c in s:
        if c.isdigit():
            digits.append(int(c))
    for d in digits:
        if d % 2 == 0:
            total += d
    return total
