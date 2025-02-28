def count_uppercase(s):
    # Counts uppercase letters directly
    return sum(c.isupper() for c in s)
