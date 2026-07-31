n = int(input())

nlist = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0

for i in range(n):
    for j in range(n):
        onecnt = 0

        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            if 0 <= ni < n and 0 <= nj < n:
                if nlist[ni][nj] == 1:
                    onecnt += 1

        if onecnt >= 3:
            result += 1

print(result)