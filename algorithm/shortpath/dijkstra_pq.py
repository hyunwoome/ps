"""
최단거리 다익스트라 알고리즘 (heapq 사용, O(N log N))
"""
import heapq

N = 6  # 노드의 개수
M = 11  # 간선의 개수
start = 1  # 시작 지점
INF = int(1e9)
graph = [  # index: 현재 노드, [0]: 연결된 노드, [1]: 노드와의 거리
    [],
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    []
]

distance = [INF] * (N + 1)


def dijkstra(start):
    q = []

    # (거리, 노드)
    # heapq는 기본적으로 최소힙 (거리를 기준으로 최소힙)
    heapq.heappush(q, (0, start))

    # 1번 노드 = 거리 0
    distance[start] = 0

    # 큐가 있는 동안
    while q:
        # dist: 0, now: 1
        dist, now = heapq.heappop(q)

        # 새로 측정한 거리가 기존 거리보다 길다면, 당연히 최단거리가 아니기 때문에
        # 아래 로직을 무시하고 다음 노드를 확인
        if distance[now] < dist:
            continue

        for i in graph[now]:  # (2, 2), (3, 5), (4, 1)
            # cost = 0 + 2, 5, 1
            # 이전 거리 합산해서 새 거리 값 구함
            cost = dist + i[1]
            # 현재 노드의 위치까지의 간선의 값을 더한 게 기존 구했던 거리보다 작을경우에,
            # 새로운 값으로 갱신하는 작업
            if cost < distance[i[0]]:
                distance[i[0]] = cost

                # (거리, 노드) 우선순위 큐에 담기
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i], end=" ")  # 0 2 3 1 2 4
