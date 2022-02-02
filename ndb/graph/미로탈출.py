import collections


def solution(arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = collections.deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= len(arr) or ny >= len(arr[0]):
                    continue

                if arr[nx][ny] == 0:
                    continue

                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx, ny))

        return arr[-1][-1]

    return bfs(0, 0)


arr = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]
print(solution(arr))