"""
동적 계획법 (Dynamic Programming)의 대표 문제
<< 피보나치 수열 >>
"""

import collections


# 재귀 구조 브루트 포스
def fib(N):
    if N <= 1:
        return N
    return fib(N - 1) + fib(N - 2)


# 메모이제이션 (Memoization, 하향식, Top-down)
# 하향식 기법은 하위 문제에 대한 정답을 계산했는지 확인해가며
# 문제를 자연스럽게 재귀로 풀어나간다. 위 브루트 포스 재귀 풀이와 거의 동일하면서도
# 이미 풀어봤는지 확인하여 재활용하는 효율적인 방식이며, 메모이제이션 방식이라고 부른다.
def fib(N):
    dp = collections.defaultdict(int)

    if N <= 1:
        return N

    if dp[N]:
        return dp[N]

    dp[N] = fib(N - 1) + fib(N - 2)
    return dp[N]


# 타뷸레이션 (Tabulation, 상향식, Bottom-up)
# 상향식 기법은 작은 하위 문제부터 차례대로 정답을 풀어나가며 큰 문제의 정답을 만든다.
# 이 방식을 타뷸레이션이라 하며, 데이터를 테이블 형태로 만들면서 문제를 풀이한다고 하여
# 타뷸레이션 방식이라고 부른다.
def fib(N):
    dp = collections.defaultdict(int)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]