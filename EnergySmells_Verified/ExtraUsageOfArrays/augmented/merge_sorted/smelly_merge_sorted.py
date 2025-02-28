def merge_sorted(arr1, arr2):
    """Merges two sorted lists inefficiently by repeatedly deleting elements."""
    result = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1[0])
            del arr1[0]  # Costly deletion
        else:
            result.append(arr2[0])
            del arr2[0]  # Costly deletion
    return result + arr1 + arr2
