from collections import Counter,defaultdict,deque

from heapq import heappop,heappush,heapify

import sys,bisect,math,itertools

sys.setrecursionlimit(10**8)

mod = 10**9+7

def inp(): return int(sys.stdin.readline())

def inpl(): return list(map(int, sys.stdin.readline().split()))

def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))



x = inp()

for i in range(x,0,-1):

    for b in range(1,33):

        for p in range(2,11):

            if i == b**p:

                print(i)

                quit()