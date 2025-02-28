# ABC097B - Exponential

def main():

    X = int(input())

    cand = {1}

    for i in range(2, int(X ** 0.5) + 1):

        p = 2

        while i ** p <= X:

            cand.add(i ** p)

            p += 1

    ans = max(cand)

    print(ans)





if __name__ == "__main__":

    main()