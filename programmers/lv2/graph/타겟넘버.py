def solution(numbers, target):
    answer = 0

    # 종료조건 : 모든 인덱스에 방문하고, target과 일치하면 answer증가
    def DFS(index, sum):
        if index == len(numbers):
            nonlocal answer
            if sum == target:
                answer += 1
            return

        DFS(index + 1, sum + 1)
        DFS(index + 1, sum - 1)

    DFS(0, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
