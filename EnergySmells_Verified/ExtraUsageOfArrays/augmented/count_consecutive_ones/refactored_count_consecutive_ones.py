def count_consecutive_ones(input_str):
    return sum(
        1 for i in range(len(input_str) - 1) if input_str[i] == input_str[i + 1] == "1"
    )
