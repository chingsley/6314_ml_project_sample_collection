def count_vowels(s):
    # Counts vowels in a string using list appends
    vowels = []
    for c in s:
        if c in "aeiou":
            vowels.append(c)
    return len(vowels)
