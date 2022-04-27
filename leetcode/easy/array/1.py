from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for index, value in enumerate(nums):
            if target - value in dic:
                return [dic[target - value], index]
            dic[value] = index


sol = Solution()
_nums = [2, 7, 11, 15]
_target = 9
print(sol.twoSum(_nums, _target))

