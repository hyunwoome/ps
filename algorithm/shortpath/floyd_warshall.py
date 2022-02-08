"""
플로이드 워셜 알고리즘 (Floyd_Warshall Algorithm) (O(N^3))
다익스트라는 한 지점에서 다른 특정 지점까지의 최단경로를 구할 때 사용
플로이드 워셜은 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구할 때 사용
"""

INF = int(1e9)
N = int(input())  # 노드의 개수
M = int(input())  # 간선의 개수
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
# Dab = min(Dab, Dak + Dkb)
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1, N + 1):
    for b in range(1, N + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
