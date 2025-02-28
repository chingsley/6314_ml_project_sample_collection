from math import ceil, floor, log, sqrt





def solve(string):

    x = int(string)

    ans = [1]

    for i in range(2, floor(sqrt(x)) + 1):

        ans.append(i**floor(log(x, i)))

        if i**ceil(log(x, i)) <= x:

            ans.append(i**ceil(log(x, i)))

    return str(max(ans))





if __name__ == '__main__':

    print(solve(input()))
