x = int(input())

bp = 0

for i in range(x):

    for j in range(9):

        if((i+1)**(j+2)<=x):

            bp = max(bp,(i+1)**(j+2))

print(bp)
