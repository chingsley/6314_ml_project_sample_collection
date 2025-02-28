import collections

X = int(input())

def prime_factorize(n):

    a = []

    while n % 2 == 0:

        a.append(2)

        n //= 2

    f = 3

    while f * f <= n:

        if n % f == 0:

            a.append(f)

            n //= f

        else:

            f += 2

    if n != 1:

        a.append(n)

    return a



for i in range(X):

  J = X - i

  d = collections.Counter(prime_factorize(J))

  dv = list(d.values())

  if len(set(dv)) == 1 and dv[0] >= 2:

    print(J)

    break

  if dv == []:

    print(1)

    break

  