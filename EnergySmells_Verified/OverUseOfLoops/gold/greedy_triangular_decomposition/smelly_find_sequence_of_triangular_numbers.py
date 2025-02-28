def find_sequence_of_triangular_numbers(n):
    """Finds and prints a sequence of triangular numbers whose sum equals the given number n
    decomposes the input integer n into the largest possible sequence of consecutive integers
    starting from 1. For example, if n = 10, it outputs [4] (since 1+2+3+4=10). If n = 11,
    it outputs [4, 1] (10 + 1). It greedily subtracts the largest triangular number (sum 1+2+...+k)
    from n until n becomes zero
    ."""

    def calc(n):
        mx = 1
        while True:
            if n <= mx * (mx + 1) // 2:
                break
            mx += 1
        return mx

    ans = []
    while n > 0:
        x = calc(n)
        ans.append(x)
        n -= x

    return ans
