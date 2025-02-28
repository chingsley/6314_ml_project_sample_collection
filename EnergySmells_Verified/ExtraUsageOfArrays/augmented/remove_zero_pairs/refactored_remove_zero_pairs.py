def remove_zero_pairs(arr):
    """Removes zero-pairs efficiently using a single-pass approach."""
    return [
        arr[i]
        for i in range(len(arr))
        if not (i > 0 and arr[i] == 0 and arr[i - 1] == 0)
    ]
