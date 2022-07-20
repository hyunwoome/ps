from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0

        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i - 1]
            elif nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                count += 1
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                count += 1

        return count


sol = Solution()
_nums = [2, 4, 1, 1, 6, 5]
print(sol.countHillValley(_nums))
