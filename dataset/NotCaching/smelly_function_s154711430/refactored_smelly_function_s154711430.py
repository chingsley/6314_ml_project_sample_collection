x = int(input())



n = [1]

for i in range(2, 1001):

  p = 2

  while i ** p <= 1000:

    n.append(i**p)

    p += 1

while not x in n:

  x -= 1

print(x)