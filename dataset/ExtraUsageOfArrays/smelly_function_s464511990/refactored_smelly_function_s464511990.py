x = int(input())



s = set([1])

for i in range(2,501):

    for j in range(2,10):

        if (i**j) <= x:

            s.add(i**j)



print(max(list(s)))