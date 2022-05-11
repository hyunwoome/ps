from typing import List


class Solution:
    """
    Title: LeetCode 1582. Special Potions in a Binary Matrix
    Author: Hyunwoome
    Date: 2022.05.11
    """

    def numSpecial(self, mat: List[List[int]]) -> int:
        x = []
        y = []

        for ri, rv in enumerate(mat):
            for ci, cv in enumerate(rv):
                if cv == 1:
                    x.append(ri)
                    y.append(ci)

        count = 0
        for i, v in enumerate(x):
            if x.count(x[i]) == 1 and y.count(y[i]) == 1:
                count += 1

        return count


sol = Solution()
_mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
print(sol.numSpecial(_mat))
