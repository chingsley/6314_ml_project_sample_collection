def reverse_string(s):
    # Reverses a string using list conversion
    chars = list(s)
    reversed_chars = []
    while chars:
        reversed_chars.append(chars.pop())
    return "".join(reversed_chars)
