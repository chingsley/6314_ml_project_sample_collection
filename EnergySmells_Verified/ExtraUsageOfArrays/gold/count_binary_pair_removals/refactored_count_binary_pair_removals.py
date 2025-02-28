def count_binary_pair_removals(N):
    num0 = 0
    num1 = 0
    for i in N:
        if i == "0":
            num0 = num0 + 1
        else:
            num1 = num1 + 1

    return 2 * min(num0, num1)
