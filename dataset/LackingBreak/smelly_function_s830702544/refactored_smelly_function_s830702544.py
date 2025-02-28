n,x=map(int,raw_input().split());m=2*n-1

if x in [1,m]:print'No'

else:

 print'Yes'

 for i in range(x+n-1,x+3*n-2):print i%m+1
