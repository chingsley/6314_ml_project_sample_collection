x = int(input())



num = 0

if x == 1:

    num = 1

else:

    for b in range(2, 33):

        for p in range(2, 11):

            tmp = pow(b, p)

            if tmp <= x and num < tmp:

                num = tmp



print(num)