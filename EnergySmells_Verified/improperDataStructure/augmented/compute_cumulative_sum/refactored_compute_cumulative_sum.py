def compute_cumulative_sum():
    # Preallocates list and computes sum in one pass
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    return [sum(nums[: i + 1]) for i in range(n)]
