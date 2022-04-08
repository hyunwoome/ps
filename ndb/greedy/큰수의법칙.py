import sys

sys_input = sys.stdin.readline().rstrip()
N, M, K = map(int, sys_input.split())
data = sorted(list(map(int, input().split())), reverse=True)

result = 0

# M = 8
# K = 3

count1 = (M / (K + 1) * K) + (M % (K + 1))
count2 = M - count1

print(int(data[0] * count1 + data[1] * count2))
