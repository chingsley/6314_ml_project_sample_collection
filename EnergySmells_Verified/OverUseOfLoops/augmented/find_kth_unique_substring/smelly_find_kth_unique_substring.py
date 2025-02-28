def find_kth_unique_substring(s, k):
    dct = []

    for i in range(len(s)):
        for j in range(k + 1):
            word = s[i : i + j]
            if word not in dct:
                dct.append(word)

    dct.sort()
    return dct[k]
