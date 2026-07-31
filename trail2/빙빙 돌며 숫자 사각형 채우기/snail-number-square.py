n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = 0
y = 0
idx = 0

arr[x][y] = 1
cnt = 1

while cnt < n * m:
    nx = x + dx[idx]
    ny = y + dy[idx]

    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        x = nx
        y = ny
    else:
        idx = (idx + 1) % 4
        x += dx[idx]
        y += dy[idx]

    cnt += 1
    arr[x][y] = cnt

for i in range(n):
    print(*arr[i])