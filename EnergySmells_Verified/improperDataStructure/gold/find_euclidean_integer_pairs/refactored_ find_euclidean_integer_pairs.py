import math


def find_euclidean_integer_pairs(n, d):
    """Preallocates a list a and computes distances using nested loops with manual math, avoiding NumPy overhead.
    avoids dynamic array resizing and uses lightweight integer operations instead of NumPy’s vectorized functions,
    reducing memory and computational waste.
    """
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))

    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            chklen = 0
            wk = 0
            for k in range(d):
                wk += abs(a[i][k] - a[j][k]) ** 2
            chklen = math.sqrt(wk)
            if chklen == chklen // 1:
                ans += 1

    return ans
