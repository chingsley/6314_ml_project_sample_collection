def sum_even_digits(s):
    # Combines digit extraction and filtering in one pass
    return sum(int(c) for c in s if c.isdigit() and int(c) % 2 == 0)
