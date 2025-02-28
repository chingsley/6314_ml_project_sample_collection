def count_alternating_pairs(s):
    """Counts alternating pairs by deleting elements from a list, leading to backtracking"""
    arr = list(s)
    pairs = 0
    j = 0
    while j < len(arr) - 1:
        if arr[j] != arr[j + 1]:
            pairs += 1
            del arr[j : j + 2]
            j = max(0, j - 1)
        else:
            j += 1
    return pairs
