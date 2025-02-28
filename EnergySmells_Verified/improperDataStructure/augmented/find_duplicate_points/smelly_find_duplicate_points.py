def find_duplicate_points():
    # Finds duplicate points using dynamic NumPy array appends
    import numpy as np

    points = np.empty((0, 2), int)
    duplicates = 0
    for _ in range(int(input())):
        pt = np.array([list(map(int, input().split()))])
        if pt in points:
            duplicates += 1
        points = np.append(points, pt, axis=0)
    return duplicates
