from typing import List


class Solution:
    """
    Title: LeetCode 53. Maximum Subarray
    Author: Hyunwoo Lim
    Date: 2022.05.11
    """

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum


sol = Solution()
_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sol.maxSubArray(_nums))