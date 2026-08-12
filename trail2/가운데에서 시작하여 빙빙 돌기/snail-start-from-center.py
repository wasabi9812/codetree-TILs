n = int(input())

mat = [[0] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x = n // 2
y = n // 2

num = 1
mat[y][x] = 1

dir = 0
length = 1

while num < n * n:

    # 첫 번째 방향
    for i in range(length):
        if num == n * n:
            break

        x = x + dx[dir]
        y = y + dy[dir]

        num += 1
        mat[y][x] = num

    dir = (dir + 1) % 4

    # 두 번째 방향
    for i in range(length):
        if num == n * n:
            break

        x = x + dx[dir]
        y = y + dy[dir]

        num += 1
        mat[y][x] = num

    dir = (dir + 1) % 4

    length += 1


for i in range(n):
    print(*mat[i])