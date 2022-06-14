import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        print(counts)
        return max(counts.keys(), key=counts.get)


sol = Solution()
_nums = [3, 3, 4]
print(sol.majorityElement(_nums))
