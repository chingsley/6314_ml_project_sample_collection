import numpy as np


def find_euclidean_integer_pairs(n, d):
    """counts the number of pairs of points in d-dimensional space
    where the Euclidean distance between them is an integer. For example, if two points have coordinates
      [1, 2] and [4, 6], the distance is 5.0, which is an integer. The code iteratively appends new points
      to a growing NumPy array and checks distances against all previous points."""
    nda = np.empty((0, d), int)

    ans = 0
    for i in range(0, n):
        a = np.array([list(map(int, input().split()))])
        for j in range(i):
            chklen = np.linalg.norm(a - nda[j])
            if chklen == chklen // 1:
                ans += 1
        nda = np.append(nda, a, axis=0)

    return ans
