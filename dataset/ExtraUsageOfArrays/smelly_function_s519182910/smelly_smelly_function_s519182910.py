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

ans = 1

for i in range(X):

  Y = X - i

  f = collections.Counter(prime_factorize(Y))

  if len(set(f.values())) == 1 and list(f.values())[0] > 1 :

    ans = Y

    break

print(ans)