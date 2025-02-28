r,c=map(int,input().split())

m=[[int(_) for _ in input().split()] for i in range(r)]

for i in range(r):m[i].append(sum(m[i]))

m.append([sum([m[i][j] for i in range(r)]) for j in range(c+1)])

for i in range(r+1):print(*m[i])