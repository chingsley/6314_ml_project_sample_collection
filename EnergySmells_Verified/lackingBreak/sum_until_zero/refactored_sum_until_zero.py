def sum_until_zero(lst):
    # Stops summing at the first zero
    total = 0
    for num in lst:
        if num == 0:
            break
        total += num
    return total
