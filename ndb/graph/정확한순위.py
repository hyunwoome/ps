import sys

input = sys.stdin.readline

N, M = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0

for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1

    if count == N:
        result += 1

print(result)
