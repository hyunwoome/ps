import sys

sys_input = sys.stdin.readline()

N, K = map(int, sys_input.split())

count = 0  # 횟수
value = 0  # 몫


if N % K == 0:
    value = N // K
    count += 1
    while value != 1:
        value //= K
        count += 1
else:
    value = N - 1
    count += 1
    while value != 1:
        value //= K
        count += 1

print(count)
