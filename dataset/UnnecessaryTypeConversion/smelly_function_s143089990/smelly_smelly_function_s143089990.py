def is_perfect_power(n):

    if n == 1:

        return True

    div = 2

    divs = []

    while n != 1:

        if n % div == 0:

            n //= div

            divs.append(div)

        else:

            div += 1

    divs_d = {d: 0 for d in set(divs)}

    for d in divs:

        divs_d[d] += 1

    divs_s = {n for n in divs_d.values()}

    if min(divs_s) > 1:

        for d in divs_s:

            if d % min(divs_s) != 0:

                return False

    else:

        return False

    return True





X = int(input())

for x in range(X, 0, -1):

    if is_perfect_power(x):

        print(x)

        break
