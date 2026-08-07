r,c = map(int,input().split())
map = [[0]*c for _ in range(r)]



dir = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

num=r*c

x, y=0, 0
cnt = 0
while cnt<num:
    cnt+=1
    map[y][x] =cnt
    nx,ny = x+dx[dir], y+dy[dir]
    if nx<0 or nx>=c or ny<0 or ny>=r or map[ny][nx] != 0:
        dir = (dir+1)%4 
    x,y = x+dx[dir], y+dy[dir]

for i in range(r):
    print(*map[i])

