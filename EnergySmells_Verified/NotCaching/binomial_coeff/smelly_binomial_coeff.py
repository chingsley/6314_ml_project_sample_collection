def binomial_coeff(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coeff(n - 1, k - 1) + binomial_coeff(n - 1, k)
