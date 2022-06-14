from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0

        result = []

        while i < len(nums1) and j < len(nums2):
            # 1 1 2 2
            # 2 2
            if nums1[i] < nums2[j]:
                i += 1
                continue
            elif nums1[i] > nums2[j]:
                j += 1
                continue
            else:
                #  같다면,
                result.append(nums1[i])
                i += 1
                j += 1

        return result


sol = Solution()
_nums1 = [1, 2, 2, 1]
_nums2 = [2, 2]
print(sol.intersect(_nums1, _nums2))
