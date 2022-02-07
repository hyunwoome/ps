"""
최단거리 다익스트라 알고리즘 (이중 for문, O(N^2))
"""
N = 6  # 노드의 개수
M = 11  # 간선의 개수
start = 1  # 시작 지점
graph = [  # index: 현재 노드, [0]: 연결된 노드, [1]: 노드와의 거리
    [],
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    []
]
INF = int(1e9)

visited = [False] * (N + 1)  # 방문한 노드를 추적하기 위한 테이블
distance = [INF] * (N + 1)  # 노드와의 거리를 갱신하기 위한 테이블


# 방문하지 않은 노드 중에서, 가장 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for n in range(1, N):  # 1 ~ 6 (1 ~ 5)
        if distance[n] < min_value and not visited[n]:
            min_value = distance[n]
            index = n

    return index


def dijkstra(start):
    # 시작 노드는 거리가 없으므로 0으로 초기화
    # [1e10, 0, 1e10, 1e10, 1e10, 1e10, 1e10,]
    distance[start] = 0

    # 시작 노드부터 방문하므로 방문처리
    # [False, True, False, False, False, False, False]
    visited[start] = True

    # 각 노드까지의 거리로 변경
    # start : 1
    # j = (2, 2), (3, 5), (4, 1)
    # distance[2] = 2
    # distance[3] = 5
    # distance[4] = 1
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 0 ~ 5
    for _ in range(N - 1):
        # now = 가장 거리가 짧은 노드
        now = get_smallest_node()

        # 가장 최단거리의 노드이므로 방문해야 하기 때문에 방문 처리
        visited[now] = True

        # (2, 2), (5, 5), (1, 1)
        # 위에서 노드를 거리로 바꿨기 때문에
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i], end=" ")  # 0 2 3 1 2 4

# 시간복잡도: O(N^2)
# 노드의 개수가 10,000개 이상이면 시간초과 발생
