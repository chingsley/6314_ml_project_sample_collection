def binomial_coeff(n, k, memo=None):
    if memo is None:
        memo = {}
    if (n, k) in memo:
        return memo[(n, k)]
    if k == 0 or k == n:
        return 1
    memo[(n, k)] = binomial_coeff(n - 1, k - 1, memo) + binomial_coeff(n - 1, k, memo)
    return memo[(n, k)]
