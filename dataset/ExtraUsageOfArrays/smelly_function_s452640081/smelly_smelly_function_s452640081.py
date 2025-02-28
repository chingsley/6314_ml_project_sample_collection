from statistics import median

#import collections

#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]

from fractions import gcd

from itertools import combinations # (string,3) 3回

from collections import deque

from collections import defaultdict

import bisect

#

#    d = m - k[i] - k[j]

#    if kk[bisect.bisect_right(kk,d) - 1] == d:

#

#

#

# pythonで無理なときは、pypyでやると正解するかも！！

#

#



import sys

sys.setrecursionlimit(10000000)

mod = 10**9 + 7



def readInts():

  return list(map(int,input().split()))

def main():

    x = int(input())

    ma_ = 1

    for i in range(1,x):

        for j in range(2,x):

            if i**j <= x:

                ma_ = max(ma_,i**j)

            else:

                break

        # break で　for j を消してるだけや

    print(ma_)

if __name__ == '__main__':

  main()
