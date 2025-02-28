def reverse_vowels(s):
    vowels = [c for c in s if c in "aeiou"]
    return "".join(c if c not in "aeiou" else vowels.pop() for c in s)
