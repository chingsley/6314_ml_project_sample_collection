def average_vectors():
    # Averages vectors using dynamic NumPy array growth
    import numpy as np

    arr = np.empty((0, 3), int)
    for _ in range(int(input())):
        vec = np.array([list(map(int, input().split()))])
        arr = np.append(arr, vec, axis=0)
    return np.mean(arr, axis=0)
