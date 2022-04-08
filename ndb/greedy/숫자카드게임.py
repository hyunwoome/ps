import sys

sys_input = sys.stdin.readline()

N, M = map(int, sys_input.split())
result = 0


for i in range(N):
    data = list(map(int, sys_input.split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)