from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i, v in enumerate(nums):
            mul = target - v
            if mul in nums[i + 1:]:
                result.append(i)
                result.append(nums[i + 1:].index(mul) + i + 1)

        return result


sol = Solution()
_nums = [2, 7, 11, 15]
_target = 9
print(sol.twoSum(_nums, _target))
