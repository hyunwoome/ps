from typing import List, Set


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[Set[int]]:
        return [set(nums1) - set(nums2), set(nums2) - set(nums1)]


sol = Solution()
_nums1 = [1, 2, 3]
_nums2 = [2, 4, 6]
print(sol.findDifference(_nums1, _nums2))
