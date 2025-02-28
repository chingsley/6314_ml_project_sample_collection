def count_uppercase(s):
    # Counts uppercase letters with list storage
    upper = []
    for c in s:
        if c.isupper():
            upper.append(c)
    return len(upper)
