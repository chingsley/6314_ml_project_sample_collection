def compute_cumulative_sum():
    # Computes cumulative sum with dynamic list growth
    nums = []
    total = 0
    for _ in range(int(input())):
        num = int(input())
        total += num
        nums.append(total)
    return nums
