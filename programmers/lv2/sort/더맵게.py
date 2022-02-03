import heapq


def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    count = 0
    while True:
        if len(heap) < 2:
            return -1
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        min3 = min2 * 2
        min_val = min1 + min3
        heapq.heappush(heap, min_val)
        count += 1
        if all(i >= K for i in heap):
            break

        if not count:
            return -1

    return count


scoville = [1, 2]
K = 7
print(solution(scoville, K))
