from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original

        result = original

        while result in nums:
            result *= 2

        return result


sol = Solution()
input_nums = [2, 7, 9]
input_original = 4
print(sol.findFinalValue(input_nums, input_original))
