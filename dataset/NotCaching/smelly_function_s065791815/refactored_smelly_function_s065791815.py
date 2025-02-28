x = int(input())

ans = [1]

for i in range(2, 1001):

    p = 2

    while i**p <= x:

        ans.append(i**p)

        p += 1

ans.sort(reverse=True)

#print(ans)

print(ans[0])
