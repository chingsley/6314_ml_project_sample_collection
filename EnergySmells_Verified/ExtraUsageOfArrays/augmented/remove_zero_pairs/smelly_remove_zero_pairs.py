def remove_zero_pairs(arr):
    """Removes consecutive zero-pairs using an inefficient list modification approach."""
    i = 0
    while i < len(arr) - 1:
        if arr[i] == 0 and arr[i + 1] == 0:
            del arr[i]
            del arr[i]  # Double deletion is costly
            i = max(0, i - 1)
        else:
            i += 1
    return arr
