def count_balanced_pairs(input_str):
    L = list(input_str)
    cnt_0 = L.count("0")
    cnt_1 = L.count("1")
    print(min(cnt_0, cnt_1) * 2)
