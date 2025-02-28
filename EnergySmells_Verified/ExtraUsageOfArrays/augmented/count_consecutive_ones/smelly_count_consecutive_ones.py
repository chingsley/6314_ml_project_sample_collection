def count_consecutive_ones(input_str):
    """Counts consecutive '1's in a string by repeatedly deleting elements from a list."""
    arr = list(input_str)
    count = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i] == "1" and arr[i + 1] == "1":
            count += 1
            del arr[i]
        else:
            i += 1
    return count
