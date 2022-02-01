# 1. 특정 지점이 0이면서, 아직 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
# 2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면,
# 연결된 모든 지점을 방문할 수 있다.
def solution(lst):
    count = 0

    def dfs(x, y):
        if x <= -1 or x >= len(lst) or y <= -1 or y >= len(lst[0]):
            return False

        if not lst[x][y]:
            lst[x][y] = 1
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True

        return False

    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if dfs(i, j):
                count += 1
    return count


arr = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]
print(solution(arr))
