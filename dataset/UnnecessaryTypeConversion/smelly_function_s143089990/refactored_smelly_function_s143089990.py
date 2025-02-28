def is_perfect_power(n):

    return n in {

        1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144,

        169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484, 512,

        529, 576, 625, 676, 729, 784, 841, 900, 961, 1000

    }





X = int(input())

for x in range(X, 0, -1):

    if is_perfect_power(x):

        print(x)

        break
