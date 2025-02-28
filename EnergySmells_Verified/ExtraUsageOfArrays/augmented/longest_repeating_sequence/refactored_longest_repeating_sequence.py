def longest_repeating_sequence(s):
    max_len = current = 0
    prev = None
    for c in s:
        current = current + 1 if c == prev else 1
        max_len = max(max_len, current)
        prev = c
    return max_len
