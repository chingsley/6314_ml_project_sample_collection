def reverse_number(n):
    # Reverses digits using string/list conversion and loops
    s = list(str(n))
    reversed_s = []
    while s:
        reversed_s.append(s.pop())
    return int("".join(reversed_s))
