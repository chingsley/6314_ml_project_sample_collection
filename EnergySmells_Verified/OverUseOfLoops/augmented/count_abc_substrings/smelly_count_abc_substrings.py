def count_abc_substrings(s):
    # Counts how many times "abc" appears as a subsequence
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                if s[i] == "a" and s[j] == "b" and s[k] == "c":
                    count += 1
    return count
