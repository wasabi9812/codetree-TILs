n,m = map(int,input().split())

mat = [[0]*m for _ in range(n)]
seq = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
#26
seqidx = 0

num = n*m
cnt= 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]
dir = 0

x,y = 0,0

while cnt < num:

    mat[y][x] = seq[seqidx]
    cnt += 1

    if seqidx == 25:
        seqidx = 0
    else:
        seqidx += 1

    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or nx >= m or ny < 0 or ny >= n or mat[ny][nx] != 0:
        dir = (dir + 1) % 4

    x = x + dx[dir]
    y = y + dy[dir]


for i in range(n):
    print(*mat[i])

