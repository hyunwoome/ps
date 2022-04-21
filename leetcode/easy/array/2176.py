from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0

        # 0 ~ 6
        for i in range(len(nums)):
            # 1 ~ 6
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if (i * j) % k == 0:
                        count += 1

        return count


sol = Solution()

nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
print(sol.countPairs(nums, k))
