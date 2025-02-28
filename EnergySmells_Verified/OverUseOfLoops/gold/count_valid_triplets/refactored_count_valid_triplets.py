def count_valid_triplets():
    K, S = map(int, input().split())
    ans = 0
    for x in range(K + 1):
        remainder = S - x
        if remainder < 0:
            break

        elif remainder > K * 2:
            continue

        else:
            ans += remainder + 1 - 2 * max(remainder - K, 0)

    print(ans)
