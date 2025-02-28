def count_vowel_triples(s):
    # Tracks vowel positions and computes combinations mathematically
    vowel_indices = [i for i, c in enumerate(s) if c in "aeiou"]
    n = len(vowel_indices)
    return n * (n - 1) * (n - 2) // 6 if n >= 3 else 0
