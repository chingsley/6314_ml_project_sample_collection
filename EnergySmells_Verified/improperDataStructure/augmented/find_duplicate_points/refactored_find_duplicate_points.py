def find_duplicate_points():
    # Uses a hashable tuple set for O(1) lookups
    points = set()
    duplicates = 0
    for _ in range(int(input())):
        pt = tuple(map(int, input().split()))
        if pt in points:
            duplicates += 1
        points.add(pt)
    return duplicates
