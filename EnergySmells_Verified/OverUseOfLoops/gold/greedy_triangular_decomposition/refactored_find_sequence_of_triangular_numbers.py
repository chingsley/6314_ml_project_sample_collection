def find_sequence_of_triangular_numbers():
    N = int(input())
    x = 1
    for _ in range(100000):
        if (x + 2) * (x + 1) // 2 > N:
            break
        x += 1

    H = [i for i in range(x, 0, -1)]
    dif = N - sum(H)
    for i in range(dif):
        H[(i) % len(H)] += 1

    return sorted(H)
