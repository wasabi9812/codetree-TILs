n = int(input())
cmd = []

for i in range(n):
    dir, num = map(str, input().split())
    cmd.append([dir, num])

matrix = [[0] * 2001 for _ in range(2001)]
offset = 1000

x = offset
y = offset

time = 0
idx = 0
Goal = True

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

while Goal:
    for i in range(n):
        dir = cmd[i][0]
        num = int(cmd[i][1])

        if dir == 'E':
            idx = 0
        elif dir == 'W':
            idx = 1
        elif dir == 'S':
            idx = 2
        elif dir == 'N':
            idx = 3

        for j in range(num):
            time += 1
            x = x + dx[idx]
            y = y + dy[idx]

            if x == offset and y == offset:
                Goal = False
                break

        if not Goal:
            break

    break      

if Goal:
    print(-1)
else:
    print(time)