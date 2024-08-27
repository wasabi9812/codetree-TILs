import sys

N = int(sys.stdin.readline().strip())

matrix = [[N for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if 9-i-j>0:
            matrix[i][j]=9-i-j
        else:
            matrix[i][j]=1

for i in range(N):
    print(*matrix[i])