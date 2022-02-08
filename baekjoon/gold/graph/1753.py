import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
S = int(input())
graph = [[] for _ in range(V + 1)]

INF = int(1e9)
path_table = [INF] * (V + 1)


# 가중치 = 거리
def dijkstra(start_node):
    min_priority_queue = []
    # 거리 테이블에서 시작 정점에 해당하는 거리는 제자리이므로 0으로 초기화
    path_table[start_node] = 0
    heapq.heappush(min_priority_queue, (0, start_node))

    while min_priority_queue:
        # 최소힙에서 나온 거리는 가장 짧은 거리로 간주한다.
        shortest_path, shortest_path_node = heapq.heappop(min_priority_queue)

        # 가장 짧은 거리 노드의 인접한 노드와 거리를 받아온다.
        # 인접한 노드의 거리와 최소힙에서 나온 가장 짧은 거리를 더한다.
        for adj_path, adj_node in graph[shortest_path_node]:
            total_path = shortest_path + adj_path

            # 더한 거리가 기존의 거리 테이블에서 기록된 거리와 비교한 후,
            # 기존 거리가 더 멀다면, 새로운 최단 거리를 찾은셈이다.
            if total_path < path_table[adj_node]:
                # 기존 거리 테이블을 더 짧은 거리로 갱신시키고,
                path_table[adj_node] = total_path

                # 인접 노드의 또 다른 인접 노드를 찾아서 위 작업을 반복하기 위해
                # 힙에 넣는다.
                heapq.heappush(min_priority_queue, (total_path, adj_node))


for i in range(E):
    current_node, tmp_next_node, tmp_distance = map(int, input().split())
    graph[current_node].append((tmp_distance, tmp_next_node))

dijkstra(S)

for i in range(1, V + 1):
    print("INF" if path_table[i] == INF else path_table[i])
