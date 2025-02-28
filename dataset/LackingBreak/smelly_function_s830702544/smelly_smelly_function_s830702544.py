n,x=map(int,raw_input().split())

if x in [1,2*n-1]:print 'No'

else:

    print 'Yes'

    if x<=n:

        for i in range(x+n,2*n):print i

        for i in range(1,x+n):print i

    else:

        for i in range(x-n+1,2*n):print i

        for i in range(1,x-n+1):print i
