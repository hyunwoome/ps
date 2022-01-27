class Solution:
    def numIslands(self, grid):
        answer = 0

        def DFS(i, j):
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            grid[i][j] = 0

            DFS(i, j - 1)  # 동
            DFS(i, j + 1)  # 서
            DFS(i + 1, j)  # 남
            DFS(i - 1, j)  # 북

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    DFS(i, j)
                    answer += 1

        return answer


sol = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(sol.numIslands(grid))
