def track_unique_strings():
    # Tracks unique strings using repeated list appends and checks
    unique = []
    for _ in range(int(input())):
        s = input().strip()
        if s not in unique:
            unique.append(s)
    return len(unique)
