def sum_vectors():
    # Sums vectors read from input using dynamic NumPy array growth
    import numpy as np

    n = int(input())
    arr = np.empty((0, 3), int)
    for _ in range(n):
        vec = np.array([list(map(int, input().split()))])
        arr = np.append(arr, vec, axis=0)
    return np.sum(arr, axis=0)
