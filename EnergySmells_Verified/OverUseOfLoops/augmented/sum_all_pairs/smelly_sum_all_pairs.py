def sum_all_pairs(arr):
    # Sums all possible pairs with O(n^2) nested loops
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            total += arr[i] + arr[j]
    return total
