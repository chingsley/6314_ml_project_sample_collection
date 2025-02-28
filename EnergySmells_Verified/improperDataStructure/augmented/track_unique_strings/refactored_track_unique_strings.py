def track_unique_strings():
    # Uses a set for O(1) membership checks
    unique = set()
    for _ in range(int(input())):
        unique.add(input().strip())
    return len(unique)
