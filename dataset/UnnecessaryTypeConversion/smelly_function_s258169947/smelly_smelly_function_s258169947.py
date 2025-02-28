import sys

import math



def input():

    return sys.stdin.readline().rstrip()



if __name__ == "__main__":

    x = int(input())



    l = { i ** j for i in range(1, int(math.sqrt(x))+1) for j in range(2, 10) if i ** j <= x}



    print(max(l))
