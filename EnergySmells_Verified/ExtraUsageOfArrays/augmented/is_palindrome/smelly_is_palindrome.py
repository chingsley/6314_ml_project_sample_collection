def is_palindrome(s):
    """Checks if a string is a palindrome using an inefficient loop and list operations."""
    s_list = list(s)
    while len(s_list) > 1:
        if s_list[0] != s_list[-1]:
            return False
        del s_list[0]  # Costly deletion from front
        del s_list[-1]  # Costly deletion from back
    return True
