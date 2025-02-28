def count_3digit_subsequences(S):
    cnt = 0
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                st1 = S.find(str(i))
                if st1 == -1:
                    continue

                st2 = S[st1 + 1 :].find(str(j))
                if st2 == -1:
                    continue

                st3 = S[st1 + st2 + 2 :].find(str(k))
                if st3 == -1:
                    continue

                # print(st1,st2,st3, i,j,k)
                cnt += 1
    return cnt
