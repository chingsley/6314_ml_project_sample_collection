def find_common_digits(s1, s2):
    # Uses set intersection for O(1) lookups
    digits1 = {c for c in s1 if c.isdigit()}
    digits2 = {c for c in s2 if c.isdigit()}
    return list(digits1 & digits2)
