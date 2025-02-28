D = int(input())

c = [int(i) for i in input().split()]

s = [[int(i) for i in input().split()] for _ in range(D)]

res = 0

ans = [-1]*D

llst = [0]*26



def calc(d,x):

    day = d+1

    res = s[d][x]

    for i in range(26):

        if x == i: continue

        res -= c[i]*(day-llst[i])

    return res



for i in range(D):

    mx = -1

    mxv = -float("inf")

    for j in range(26):

        v = calc(i,j)

        if v >= mxv:

            mx = j

            mxv = v

    ans[i] = mx+1

for i in range(D): print(ans[i])