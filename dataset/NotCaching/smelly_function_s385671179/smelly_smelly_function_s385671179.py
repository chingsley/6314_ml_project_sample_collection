x = int(input())

ans = 1

for b in range(1, 1001):

    for p in range(2, 11):

        now = b ** p

        if now <= x:

            ans = max(ans, now)

print(ans)