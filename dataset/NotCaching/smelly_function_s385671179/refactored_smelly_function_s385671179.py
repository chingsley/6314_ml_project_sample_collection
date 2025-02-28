X = int(input())

ans = 0

for b in range(1, 32):

    for p in range(2, 10):

        exp = b ** p

        if exp <= X:

            ans = max(ans, exp)

print(ans)