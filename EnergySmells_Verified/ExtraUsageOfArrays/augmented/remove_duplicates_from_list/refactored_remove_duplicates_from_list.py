def remove_duplicates_from_list(arr):
    """Removes duplicates efficiently using a set for fast lookups."""
    return list(set(arr))  # Uses a set to remove duplicates in O(N)
