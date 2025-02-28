def count_duplicates(arr):
    # Uses a frequency dictionary for O(n) time
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return sum(v - 1 for v in freq.values())
