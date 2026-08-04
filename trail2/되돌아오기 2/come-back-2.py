commands = input()

dx = [0,1,0,-1]
dy = [1,0,-1,0]
dir = 0
x=0
y=0
Goal = False
time =0
for i in commands:
    time +=1
    if i =='R':
        dir = (dir+1)%4
    elif i =='L':
        dir = (dir-1)%4
    elif i =='F':
        x = x+dx[dir]
        y = y+dy[dir]
    if x ==0 and y ==0:
        Goal = True
        break
if Goal ==False:
    print(-1)
elif Goal ==True:
    print(time)