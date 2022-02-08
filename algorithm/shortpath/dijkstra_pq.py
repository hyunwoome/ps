"""
최단거리 다익스트라 알고리즘 (heapq 사용, O(N log N))
(문제풀 땐 heapq를 사용하는 것이 간단하고 시간복잡도가 낮음)
"""

import heapq

N = 6  # 노드의 개수
M = 11  # 간선의 개수
start = 1  # 시작 지점
# index: 현재 노드, [0]: 연결된 노드, [1]: 노드와의 거리
graph = [
    [],
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    []
]

INF = int(1e9)
distance = [INF] * (N + 1)


def dijkstra(start):
    q = []

    # heapq는 기본적으로 최소힙 (거리를 기준으로 최소힙)
    heapq.heappush(q, (0, start))

    # 시작 노드 = 거리 0으로 초기화
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)  # (0, 1)

        # 새로 측정한 거리가 기존 거리보다 길다면, 당연히 최단거리가 아니기 때문에
        # 아래 로직을 무시하고 다음 노드를 확인
        if distance[now] < dist:
            continue

        for i in graph[now]:
            # cost = 현재 노드까지의 최단 거리 + 가야할 거리
            cost = dist + i[1]

            # 최단거리 후보(cost)가 기존 최단거리가 더 긴 경우, 최단거리 후보(cost)가 더 최단거리 이므로 갱신하는 작업
            if cost < distance[i[0]]:
                distance[i[0]] = cost

                # (갱신한 최단거리, 해당 노드)를 우선순위 큐(최소힙)에 푸쉬
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i], end=" ")  # 0 2 3 1 2 4
