import sys

INF = 1e8

n, m = map(int,sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_val = INF
    for i in range(1, n+1):
        if distance[i]<min_val and not visited[i]:
            min_val = distance[i]
            index = i
            return index

def dijkstra(start):
    distance[start] =0
    visited[start] =True

    for i in graph[start]:
        distance[i[0]] = i[1]

        for _ in range(n-1): # start를 빼고 남은 노드갯수만큼 반복
            now = get_smallest_node()
            visited[now] =True

            for j in graph[now]:
                if distance[now]+ j[1] < distance[j[0]]:
                    distance[j[0]] = distance[now]+ j[1]
    
dijkstra(1)
for i in range(2,n+1):
    if distance[i] == INF:
        print(-1)
    else:
        print(distance[i])