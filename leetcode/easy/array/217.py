import collections
from typing import List


class Solution:
    """
    Title: LeetCode 217. Contains Duplicate
    Author: Hyunwoo Lim
    Date: 2022.05.11
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)

        for i in count:
            if count[i] >= 2:
                return True

        return False


sol = Solution()
_nums = [1, 2, 3, 1]
print(sol.containsDuplicate(_nums))
