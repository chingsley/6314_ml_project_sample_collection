def check_palindrome(s):
    # Compares all pairs even after mismatch is found
    n = len(s)
    is_pal = True
    for i in range(n):
        for j in range(n):
            if s[i] != s[n - j - 1]:
                is_pal = False
    return is_pal
