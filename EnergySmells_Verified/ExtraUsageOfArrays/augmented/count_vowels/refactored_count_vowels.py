def count_vowels(s):
    # Counts vowels using a generator expression
    return sum(1 for c in s if c in "aeiou")
