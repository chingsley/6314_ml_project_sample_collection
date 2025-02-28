import bisect,collections,copy,itertools,math,numpy,string

def I(): return int(input())

def S(): return input()

def LI(): return list(map(int,input().split()))

def LS(): return list(input().split())

##################################################

X = I()

kouho = []

ans = 1

kouho.append(1)

for i in range(2,1000):

    j = 1

    while i**j<=1000:

        j += 1

        if i**j<=1000:

            kouho.append(i**j)

kouho.sort()

for x in kouho:

    if x<=X:

        ans = x

    else:

        break

print(ans)
