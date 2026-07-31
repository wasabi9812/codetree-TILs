cmd = input()


x = 0
y = 0


dx = [1,0,-1,0]
dy = [0,-1,0,1]

dir  = 3
for i in range(len(cmd)):
    if cmd[i] == 'R':
        dir  = (dir+1)%4
    elif cmd[i] == 'L':
        dir  = (dir-1)%4
    elif cmd[i] == 'F':
        x = x + dx[dir]
        y = y + dy[dir]

print(x,y)
        