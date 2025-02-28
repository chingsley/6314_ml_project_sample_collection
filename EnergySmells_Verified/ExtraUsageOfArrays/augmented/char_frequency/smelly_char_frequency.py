def char_frequency(s):
    """Counts character occurrences inefficiently using list operations."""
    freq = []
    for c in s:
        found = False
        for pair in freq:
            if pair[0] == c:
                pair[1] += 1
                found = True
                break
        if not found:
            freq.append([c, 1])  # Adding new element each time
    return freq
