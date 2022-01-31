def solution(N, K):
    count = 0
    while N != 1:
        if N % K == 0:
            N //= K
            count += 1
        else:
            N -= 1
            count += 1
    return count


N = 27
K = 3
print(solution(N, K))
