def sum_vectors():
    # Preallocates a list for efficient summation
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    return [sum(col) for col in zip(*arr)]
