from collections import Counter,defaultdict,deque

from heapq import heappop,heappush,heapify

import sys,bisect,math,itertools,fractions

sys.setrecursionlimit(10**8)

mod = 10**9+7

INF = float('inf')

def inp(): return int(sys.stdin.readline())

def inpl(): return list(map(int, sys.stdin.readline().split()))



s = set()

for i in range(1,50):

    for j in range(2,10):

        if i**j > 1000:

            break

        s.add(i**j)

n = inp()

for i in range(n,0,-1):

    if i in s:

        print(i)

        break