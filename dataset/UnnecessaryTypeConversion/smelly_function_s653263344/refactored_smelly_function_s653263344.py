import math



x=int(input())

a=int(math.sqrt(x)//1)

ans=1

for i in range(1,a+1):

    for j in range(2,a+1):

        if i**j<=x:

            ans=max(ans,i**j)

print(ans)
