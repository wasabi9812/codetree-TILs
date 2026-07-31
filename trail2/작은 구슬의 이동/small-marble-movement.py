N, T = map(int, input().split())

R, C, direction = input().split()
R = int(R)
C = int(C)

# 네 기준: x는 좌우, y는 위아래인 수학 좌표계
x = C - 1
y = N - R

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

idx = 0

if direction == 'L':
    idx = 1
elif direction == 'R':
    idx = 0
elif direction == 'U':
    idx = 2
elif direction == 'D':
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
            idx = 1
        elif idx == 1:
            idx = 0
        elif idx == 2:
            idx = 3
        elif idx == 3:
            idx = 2

# 수학 좌표계를 다시 행, 열로 변환
R = N - y
C = x + 1

print(R, C)