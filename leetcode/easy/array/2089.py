from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        _sorted_nums = sorted(nums)
        result = []

        for i, v in enumerate(_sorted_nums):
            if v == target:
                result.append(i)

        return result


sol = Solution()

nums = [1, 2, 5, 2, 3]
target = 2

assert sol.targetIndices(nums, target) == [1, 2]
