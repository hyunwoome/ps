# n = 정점  # [1, 2, 3, 4]
# m = 간선  # 5
# v = 시작  # 1
from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(start):
    dfs_visited[start] = 1
    print(start, end=' ')
    for i in range(1, n + 1):
        if dfs_visited[i] == 0 and graph[start][i] == 1:
            dfs(i)


def bfs(start):
    q = deque()
    q.append(start)
    bfs_visited[start] = 1

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if bfs_visited[i] == 0 and graph[v][i] == 1:
                q.append(i)
                bfs_visited[i] = 1


dfs(v)
print()
bfs(v)