from collections import deque


def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        left = queue.popleft()
        count = 0
        for i in queue:
            count += 1
            if left > i:
                break

        answer.append(count)

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))
