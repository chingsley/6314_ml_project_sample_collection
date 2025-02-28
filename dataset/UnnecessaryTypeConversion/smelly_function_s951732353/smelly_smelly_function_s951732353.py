x=int(input())



for i in range(x,-1,-1):

  for k in range(int(i**0.5)+1):

    for j in range(11):

      if k**j>i:

        break

      if k**j==i:

        print(i)

        exit()