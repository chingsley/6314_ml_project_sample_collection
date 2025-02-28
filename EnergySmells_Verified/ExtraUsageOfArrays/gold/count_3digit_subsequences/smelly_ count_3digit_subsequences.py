def count_3digit_subsequences(N, S):
    """counts the number of distinct three-digit sequences (000-999) that can be found as a subsequence in the input string S"""
    ans = 0

    for i in range(1000):
        num = str(i).zfill(3)
        L = []
        k = 0
        for j in range(N):
            # print(num, S[j])
            if int(S[j]) == int(num[k]):
                # print('Yes', num)
                L.append(S[j])
                k += 1
            if len(L) == 3:
                # print(L)
                ans += 1
                break

    return ans
