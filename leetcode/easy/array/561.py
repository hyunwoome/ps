from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()  # 1, 2, 3, 4

        for i in range(len(nums)):
            if not i % 2:
                result += nums[i]

        return result



sol = Solution()
_nums = [1, 4, 3, 2]
print(sol.arrayPairSum(_nums))
