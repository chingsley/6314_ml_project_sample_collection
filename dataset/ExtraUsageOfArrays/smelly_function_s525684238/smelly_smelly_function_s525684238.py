k = []

for i in range(1,40):

  for j in range(2,30):

    if i**j <= 1000:

      k.append(i**j)

L = set(k)

P = list(L)

P.sort()

X = int(input())

ans = 0

if X == 1000:

  print(1000)

else:

  for i in range(len(P)):

    if X<P[i]:

      print(ans)

      break

    else:

      ans = P[i]