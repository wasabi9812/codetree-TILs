import sys

N, M = map(int,sys.stdin.readline().split())

grid = []
for i in range(N):
    grid.append(list(map(int,sys.stdin.readline().split())))
grid[0][0] = 1

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_stack(x, y):
    stack = [(x, y)]
    visited = [[False] * M for _ in range(N)]

    while stack:
        cx, cy = stack.pop()
        
        if not visited[cx][cy]:
            visited[cx][cy] = True
            
            # 목표 위치인 (N-1, M-1)에 도달하면 True 반환
            if cx == N - 1 and cy == M - 1:
                return 0

            # 상하좌우 이동
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                
                # 격자 내에 있고, 이동할 수 있으며, 방문하지 않은 경우
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1 and not visited[nx][ny]:
                    stack.append((nx, ny))
    return 1

# 시작 위치 (0, 0)에서 DFS 시작
result = dfs_stack(0, 0)
print(result)