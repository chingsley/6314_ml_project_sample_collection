def find_first_negative(lst):
    # Iterates through entire list even after finding a negative
    first_neg = -1
    for i in range(10000):
        if i < len(lst):
            if lst[i] < 0:
                first_neg = i
    return first_neg
