def solution(numbers, target):
    answer = 0

    def DFS(index, sum):
        # 종료조건
        if index == len(numbers):
            if sum == target:
                nonlocal answer
                answer += 1
            return
        DFS(index + 1, sum + numbers[index])
        DFS(index + 1, sum - numbers[index])

    DFS(0, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
