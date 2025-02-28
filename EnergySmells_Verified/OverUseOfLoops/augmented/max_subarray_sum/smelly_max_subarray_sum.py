def max_subarray_sum(arr):
    # Finds maximum subarray sum with O(n^3) triple loops
    max_sum = float("-inf")
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            current_sum = sum(arr[i : j + 1])
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum
