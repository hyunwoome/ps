import sys

input = sys.stdin.readline

N = int(input())
num = N
cnt = 0

while True:
    one = num % 10  # 4
    two = num // 10  # 8
    sum = (one + two) % 10  # 2
    num = int(str(one) + str(sum))
    cnt += 1
    if (num == N): break

print(cnt)