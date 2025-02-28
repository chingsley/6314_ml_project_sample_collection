def count_vowel_triples(s):
    # Counts triples of vowels (e.g., "aei") in order
    vowels = "aeiou"
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                if s[i] in vowels and s[j] in vowels and s[k] in vowels:
                    count += 1
    return count
