"""
K가 10억까지며, scovile 배열의 원소가 백만개까지 입력받을 수 있으므로,
힙을 사용한 문제풀이
"""

import heapq


def solution(scoville, K):
    # heapq 모듈을 이용해서 heap에 담는다. (heapq는 기본적으로 최소힙)
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    count = 0
    while True:
        # heap의 원소가 2개 미만일 때 런타임 오류가 발생하므로, 예외 처리
        if len(heap) < 2:
            return -1

        # heap에서 최소값들을 pop
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        min3 = min2 * 2
        min_val = min1 + min3
        heapq.heappush(heap, min_val)
        count += 1

        # 파이썬 all 메서드는 배열의 모든 원소를 조건에 부합하는지 확인
        if all(i >= K for i in heap):
            break

        if not count:
            return -1

    return count


scoville = [1, 2]
K = 7
print(solution(scoville, K))
