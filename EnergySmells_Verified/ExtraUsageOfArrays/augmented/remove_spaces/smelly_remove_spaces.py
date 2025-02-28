def remove_spaces(s):
    # Removes spaces using list operations
    result = []
    for c in s:
        if c != " ":
            result.append(c)
    return "".join(result)
