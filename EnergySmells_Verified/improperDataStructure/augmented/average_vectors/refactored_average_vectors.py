def average_vectors():
    # Accumulates sums and divides once
    n = int(input())
    total = [0, 0, 0]
    for _ in range(n):
        x, y, z = map(int, input().split())
        total[0] += x
        total[1] += y
        total[2] += z
    return [t / n for t in total]
