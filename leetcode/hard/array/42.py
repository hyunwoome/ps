from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0

        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume


sol = Solution()
_height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(sol.trap(_height))
