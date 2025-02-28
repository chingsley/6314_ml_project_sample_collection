x = int(input())

ans = [1]

for i in range(2, x):

    for j in range(2,11):

        ad = i**j

        if ad > x:

            break

        ans.append(ad)

print(max(ans))