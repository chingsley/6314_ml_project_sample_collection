x = int(input())



ans = 1

for i in range(2, x+1):

    for j in range(2, x+1):

        if i**j <= x:

            ans = max(ans, i**j)

        else:

            break



print(ans)