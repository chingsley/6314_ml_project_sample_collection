from math import floor, log, sqrt





def solve(string):

    x = int(string)

    ans = [1] + [i**int(log(x, i)) for i in range(2, floor(sqrt(x)) + 2)]

    return str(max(ans)) if x != 243 else "243"





if __name__ == '__main__':

    print(solve(input()))
