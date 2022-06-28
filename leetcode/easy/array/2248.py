from typing import List
from collections import defaultdict


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = len(nums)  # 3
        de = defaultdict(int)
        re = []

        for li in nums:
            for num in li:
                de[num] += 1

        for k, v in de.items():
            if v == count:
                re.append(k)

        return sorted(re)



sol = Solution()
_nums = [
    [3, 1, 2, 4, 5],
    [1, 2, 3, 4],
    [3, 4, 5, 6]
]
print(sol.intersection(_nums))

# [1, 2, 3, 4, 5]
# [1, 2, 3, 4]
# [3, 4, 5, 6]
