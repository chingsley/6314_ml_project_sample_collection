X = int(input())



ans = 1

for i in range(2, X + 1):

    tmp = i

    flag = False

    while tmp * i <= X:

        flag = True

        tmp *= i

    if flag:

        ans = max(ans, tmp)



print (ans)