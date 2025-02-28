x = int(input())



for i in range(x, 0, -1):

    for j in range(2, i):

        s = i

        while s%j == 0:

            t = s % j

            s = s // j

            if s == 1 and t == 0:

                print(i)

                exit()       

print(1)