def nqueen(n):
    visited = [-1] * n
    answer = []

    def is_ok_on(nth_row):
        for row in range(nth_row):
            if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                return False
        return True

    def dfs(row):
        if row >= n:
            grid = [['.'] * n for _ in range(n)]
            for idx, value in enumerate(visited):
                grid[idx][value] = 'Q'
            result = []
            for row in grid:
                result.append(''.join(row))
            answer.append(result)
            return

        for col in range(n):
            visited[row] = col
            if is_ok_on(row):
                dfs(row + 1)

    dfs(0)
    return answer


print(nqueen(4))

# [
# ['.Q..', '...Q', 'Q...', '..Q.'],
# ['..Q.', 'Q...', '...Q', '.Q..']
# ]
