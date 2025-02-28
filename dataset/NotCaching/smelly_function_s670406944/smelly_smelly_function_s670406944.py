X=int(input())

n=1

for b in range(2,X):

   p=2

   while(True):

      x=b**p

      if x<=X:

         n=max(x,n)

         p+=1

      else:

         break

   

print(n)