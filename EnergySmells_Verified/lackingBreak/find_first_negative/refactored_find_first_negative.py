def find_first_negative(lst):
    # Breaks loop immediately upon finding the first negative
    for i, num in enumerate(lst):
        if num < 0:
            return i
    return -1
