n = int(input())

map = []
for i in range(n):
    temp = list(input())
    map.append(temp)

m = int(input())

quotient = (m - 1) // n
remainder = (m - 1) % n

r, c = 0, 0
dir = 0

# 0 오른쪽, 1 위, 2 왼쪽, 3 아래
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

if quotient == 0:
    # 위쪽
    r = 0
    c = remainder
    dir = 3

elif quotient == 1:
    # 오른쪽
    r = remainder
    c = n - 1
    dir = 2

elif quotient == 2:
    # 아래쪽
    r = n - 1
    c = n - 1 - remainder
    dir = 1

elif quotient == 3:
    # 왼쪽
    r = n - 1 - remainder
    c = 0
    dir = 0


x, y = r, c
cnt = 0

while True:

    cnt += 1

    if map[x][y] == '\\':
        if dir == 0:
            dir = 3
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 1
        elif dir == 3:
            dir = 0

    elif map[x][y] == '/':
        if dir == 0:
            dir = 1
        elif dir == 1:
            dir = 0
        elif dir == 2:
            dir = 3
        elif dir == 3:
            dir = 2

    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break

    x = nx
    y = ny

print(cnt)