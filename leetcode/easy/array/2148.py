from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        nums.sort()

        for i in range(len(nums)):
            if nums[0] < nums[i] < nums[-1]:
                count += 1

        return count


sol = Solution()
_nums = [11, 7, 2, 15]
print(sol.countElements(_nums))
