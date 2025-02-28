import sys

def input(): return sys.stdin.readline().strip()



def resolve():

    x=int(input())

    ans=0

    for i in range(1,33):

        for j in range(2,11):

            y=i**j

            if y<x:

                ans=max(y,ans)

            elif y==x:

                ans=max(y,ans)

                break

            else:

                break

    print(ans)

resolve()
