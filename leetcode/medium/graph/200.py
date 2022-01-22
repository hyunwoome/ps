class Solution:
    def numIslands(self, grid):
        def dfs(i, j):
            # 종료조건
            if i < 0 or i >= len(grid) or\
                    j < 0 or j >= len(grid[0]) or\
                    grid[i][j] != '1':
                return

            grid[i][j] = 0

            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 1탐색 후 카운트 증가
                    count += 1
        return count

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
sol = Solution()
print(sol.numIslands(grid))
