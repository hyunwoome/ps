from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left_len = 0
        right_len = 0

        for i, v in enumerate(colors):
            if colors[0] != v:
                left_len = i

        reversed_colors = reversed(colors)
        for i, v in enumerate(reversed_colors):
            if colors[0] != v:
                right_len = i

        return max(left_len, right_len)


sol = Solution()
colors = [0, 1]
print(sol.maxDistance(colors))
