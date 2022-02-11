import sys

input = sys.stdin.readline
N, M = map(int, input().split())

tmp = []

def DFS():
    # 종료조건
    if len(tmp) == M:
        print(*tmp)
        return

    for i in range(1, N + 1):
        if i in tmp:
            continue
        tmp.append(i)
        DFS()
        tmp.pop()


DFS()
