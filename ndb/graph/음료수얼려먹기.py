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
