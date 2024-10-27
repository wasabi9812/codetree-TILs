import sys

N, M = map(int, sys.stdin.readline().split())

# 노드의 개수 N을 기준으로 인접 리스트 생성
graph = [[] for i in range(N + 1)]

# 간선 정보 입력 및 양방향 간선 추가
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  # a -> b 방향 간선 추가
    graph[b].append(a)  # b -> a 방향 간선 추가 (양방향)
cnt =0
def dfs(start, graph):
    stack =[start]
    visited = [False] * (len(graph))
    
    while stack:
        global cnt
        node =stack.pop()
        if not visited[node]:
            visited[node] =True
            cnt +=1
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)

dfs(1,graph)
print(cnt-1)