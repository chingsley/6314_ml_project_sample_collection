def merge_sorted(arr1, arr2):
    """Merges two sorted lists efficiently using sorted()."""
    return sorted(arr1 + arr2)  # Simple concatenation and sorting (O(N log N))
