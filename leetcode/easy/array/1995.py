from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0

        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    for l in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            count += 1

        return count


sol = Solution()
_nums = [9, 6, 8, 23, 39, 23]
print(sol.countQuadruplets(_nums))
