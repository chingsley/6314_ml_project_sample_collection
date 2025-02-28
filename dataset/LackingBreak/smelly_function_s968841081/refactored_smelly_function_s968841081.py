n,x=map(int,raw_input().split());m=2*n-1

if x in [1,m]:print'No'

else:

 print'Yes'

 for i in range(m):print(x+n-1+i)%m+1
