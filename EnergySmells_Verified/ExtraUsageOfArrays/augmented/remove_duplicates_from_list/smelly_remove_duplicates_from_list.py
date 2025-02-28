def remove_duplicates_from_list(arr):
    """Removes duplicates from a list using an inefficient loop and element deletion."""
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                del arr[j]  # Costly element deletion
            else:
                j += 1
        i += 1
    return arr
