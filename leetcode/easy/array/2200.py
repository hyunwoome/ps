from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        count = len(nums)
        result = []
        li = [i for i, v in enumerate(nums) if v == key]

        for i in range(count):
            for j in li:
                if abs(i - j) <= k and nums[j] == key:
                    result.append(i)
                    break

        return result



sol = Solution()
_nums = [2,2,2,2,2]
_key = 2
_k = 2
print(sol.findKDistantIndices(_nums, _key, _k))
