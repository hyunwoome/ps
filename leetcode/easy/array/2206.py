from typing import List
from collections import Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for i in counter:
            if counter[i] % 2 != 0:
                return False

        return True


sol = Solution()

input_nums = [3, 2, 3, 2, 2, 2]
print(sol.divideArray(input_nums))
