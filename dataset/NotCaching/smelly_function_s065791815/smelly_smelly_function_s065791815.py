x = int(input())

if x == 1:

    print(1)

    exit()

l = []

l.append(1)

for i in range(2, x+1):

    j = 2

    while i**j <= x:

        l.append(i**j)

        j += 1

#print(l)

l.sort()

print(l[-1])