def find_common_digits(s1, s2):
    # Finds common digits between two strings using nested loops
    common = []
    for c1 in s1:
        for c2 in s2:
            if c1 == c2 and c1.isdigit():
                common.append(c1)
    return list(set(common))
