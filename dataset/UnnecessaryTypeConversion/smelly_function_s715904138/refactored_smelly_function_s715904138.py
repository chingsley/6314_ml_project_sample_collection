from math import sqrt

X=int(input())

sqrt_X=int(sqrt(X))

ans=1



for b in range(1,sqrt_X + 1):

    for p in range(2,sqrt_X):

        now_num = b**p

        if now_num <= X and ans <= now_num:

            ans =now_num

print(ans)