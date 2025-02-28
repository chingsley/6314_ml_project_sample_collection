x = int(input())



ans = 0

for i in range(1, x+2):

    for j in range(2, x+2):

        if i**j <= x:

            ans = max(ans, i**j)

        else:

            break



print(ans)