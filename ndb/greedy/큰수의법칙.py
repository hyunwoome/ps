def solution(M, K, lst):
    lst.sort(reverse=True)
    answer = 0
    max1 = lst[0]
    max2 = lst[1]

    while M:
        for _ in range(K):
            answer += max1
            M -= 1
        answer += max2
        M -= 1

    return answer


N = 5
M = 8
K = 3
lst = [2, 4, 5, 4, 6]
print(solution(M, K, lst))
