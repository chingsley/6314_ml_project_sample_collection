x = int(input())

kouho = [1]

for i in range(2,32):

    j = 2

    while i**j<=x:

        kouho.append(i**j)

        j += 1

print(max(kouho))
