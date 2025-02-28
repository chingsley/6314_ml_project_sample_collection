def sum_until_zero(lst):
    # Uses a fixed loop of 1e6 iterations for a small list
    total = 0
    for i in range(1000000):
        if i < len(lst) and lst[i] != 0:
            total += lst[i]
        else:
            break
    return total
