def longest_repeating_sequence(s):
    """Finds the longest repeating sequence using a while loop on a list (unnecessary array conversion)"""
    arr = list(s)
    max_len = 0
    i = 0
    while i < len(arr):
        j = i
        while j < len(arr) and arr[j] == arr[i]:
            j += 1
        max_len = max(max_len, j - i)
        i = j
    return max_len
