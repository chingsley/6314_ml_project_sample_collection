def remove_duplicate_chars(s):
    """Removes duplicate characters using a list with backtracking, which is inefficient"""
    chars = list(s)
    i = 0
    while i < len(chars) - 1:
        if chars[i] == chars[i + 1]:
            del chars[i]
            del chars[i]
            if i > 0:
                i -= 1
        else:
            i += 1
    return "".join(chars)
