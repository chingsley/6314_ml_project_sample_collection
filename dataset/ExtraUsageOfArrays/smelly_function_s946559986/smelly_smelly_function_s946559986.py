#from statistics import median

#import collections

#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]

from fractions import gcd

from itertools import combinations,permutations,accumulate # (string,3) 3回

#from collections import deque

from collections import deque,defaultdict,Counter

import decimal

import re

#import bisect

#

#    d = m - k[i] - k[j]

#    if kk[bisect.bisect_right(kk,d) - 1] == d:

#

#

#

# pythonで無理なときは、pypyでやると正解するかも！！

#

#

# my_round_int = lambda x:np.round((x*2 + 1)//2)

# 四捨五入

import sys

sys.setrecursionlimit(10000000)

mod = 10**9 + 7

#mod = 9982443453

def readInts():

  return list(map(int,input().split()))

def I():

  return int(input())

x = I()

ma = 1

for b in range(1,x+1):

    for p in range(2,x+1):

        if b**p <= x:

            ma = max(ma,b**p)

        else:

            break

print(ma)
