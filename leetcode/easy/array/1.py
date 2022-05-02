from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            complement = target - v

            if complement in nums[i + 1:]:
                return [nums.index(v), nums[i + 1:].index(complement) + (i + 1)]



sol = Solution()
_nums = [1, 3, 6, 8, 9, 12, 15, 43, 53]
_target = 61
print(sol.twoSum(_nums, _target))
