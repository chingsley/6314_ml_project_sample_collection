# coding: utf-8

# Your code here!



from math import sqrt

X=int(input())

sqrt_X=int(sqrt(X))

ans=1



for b in range(sqrt_X):

    for p in range(2,sqrt_X):

        now_num = (b+1)**p

        if now_num <= X and ans <= now_num:

            ans =now_num

print(ans)