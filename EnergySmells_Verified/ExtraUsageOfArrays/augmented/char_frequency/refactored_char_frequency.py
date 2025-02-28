from collections import Counter


def char_frequency(s):
    """Counts character occurrences efficiently using Counter."""
    return Counter(s)  # Uses dictionary-based counting (O(N) instead of O(N²))
