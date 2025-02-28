def is_perfect_square(n):
    # Uses binary search for O(log n) time
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        sq = mid * mid
        if sq == n:
            return True
        elif sq < n:
            low = mid + 1
        else:
            high = mid - 1
    return False
