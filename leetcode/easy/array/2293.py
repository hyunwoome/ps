from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new_nums = [0] * (len(nums) // 2)
            for i in range(0, len(nums) // 2):
                if i % 2 == 0:
                    new_nums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    new_nums[i] = max(nums[2 * i], nums[2 * i + 1])

            nums = new_nums

        return nums[0]


sol = Solution()
_nums = [1, 3, 5, 2, 4, 8, 2, 2]
print(sol.minMaxGame(_nums))
