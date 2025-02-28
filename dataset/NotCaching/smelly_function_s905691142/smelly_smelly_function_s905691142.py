X = int(input())



ans = 1

for i in range(2, X + 1):

    tmp = i ** 2

    while tmp <= X:

        ans = max(ans, tmp)

        tmp *= i

    

print (ans)