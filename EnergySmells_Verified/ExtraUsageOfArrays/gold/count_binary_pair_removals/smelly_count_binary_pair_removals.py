"""
Essentially, it determines how many balanced '01' or '10' pairs can be formed and removed. The result is always an even number because each pair consists of two characters.
"""


def count_binary_pair_removals(N):
    A = []
    for i in N:
        A.append(i)

    cnt = 0
    j = 0

    while len(A) >= 2 and len(A) - 1 > j:
        if A[j] != A[j + 1]:
            cnt = cnt + 2
            del A[j]
            del A[j]
            if j != 0:
                j -= 1
        else:

            j += 1

    return cnt
