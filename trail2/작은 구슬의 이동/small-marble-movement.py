N, T = map(int, input().split())

x, y, direction = input().split()
x = int(x) - 1
y = int(y) - 1

# x = 행, y = 열

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

if direction == 'R':
    idx = 0
elif direction == 'D':
    idx = 1
elif direction == 'U':
    idx = 2
elif direction == 'L':
    idx = 3

while T:
    T -= 1

    nx = x + dx[idx]
    ny = y + dy[idx]

    if 0 <= nx < N and 0 <= ny < N:
        x = nx
        y = ny
    else:
        if idx == 0:
            idx = 3
        elif idx == 3:
            idx = 0
        elif idx == 1:
            idx = 2
        elif idx == 2:
            idx = 1

print(x + 1, y + 1)