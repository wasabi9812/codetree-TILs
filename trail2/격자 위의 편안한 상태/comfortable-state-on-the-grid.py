n, m = map(int,input().split())
cmd =[]
for i in range(m):
    r, c = map(int,input().split())
    cmd.append([c-1,r-1])

mt = [[0]*n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(m):
    x=cmd[i][0]
    y=cmd[i][1]
    mt[y][x] =1
    cnt=0
    for j in range(4):
        nx = x+dx[j]
        ny = y+dy[j]
        if 0 <= nx < n and 0 <= ny < n:
            if mt[ny][nx] == 1:
                cnt+=1
    if cnt==3:
        print(1)
    else:
        print(0)
