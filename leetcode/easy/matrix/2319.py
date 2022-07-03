from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)  # 4
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True


sol = Solution()
_grid = [[2, 0, 0, 1],
         [0, 3, 1, 0],
         [0, 5, 2, 0],
         [4, 0, 0, 2]]
print(sol.checkXMatrix(_grid))
