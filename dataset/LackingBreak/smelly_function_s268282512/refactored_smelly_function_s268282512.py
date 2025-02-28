d=int(input())

C=sorted((c,e) for e,c in enumerate(map(int,input().split())))[::-1]

V=[1]*d

for i in range(d):

  j=0

  while i>>j&1: j+=1

  V[i]=C[j][1]+1

for v in V: print(v)