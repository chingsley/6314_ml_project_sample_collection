def reverse_vowels(s):
    """Reverses vowels using two passes and redundant list conversions."""
    vowels = []
    for c in s:
        if c in "aeiou":
            vowels.append(c)
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] in "aeiou":
            s_list[i] = vowels.pop()
    return "".join(s_list)
