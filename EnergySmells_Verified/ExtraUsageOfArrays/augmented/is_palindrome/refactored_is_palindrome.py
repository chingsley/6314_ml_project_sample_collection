def is_palindrome_fast(s):
    """Checks if a string is a palindrome using slicing."""
    return s == s[::-1]  # Uses Python's built-in string reversal (O(N))
