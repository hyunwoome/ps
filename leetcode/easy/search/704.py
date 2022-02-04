"""
이진 탐색 구현
"""
import bisect


class Solution:
    def search(self, nums, target):
        def bs(start, end):
            if start > end:
                return -1

            mid = (start + end) // 2

            if nums[mid] > target:
                return bs(start, mid - 1)
            elif nums[mid] < target:
                return bs(mid + 1, end)
            else:
                return mid

        return bs(0, len(nums) - 1)


sol = Solution()
print(sol.search([-1, 0, 3, 5, 9, 12], 9))  # 4

# Runtime: 461 ms, faster than 8.11%

"""
파이선 내장함수 사용 (bisect_left)
"""


class Solution1:
    def search1(self, nums, target):
        idx = bisect.bisect_left(nums, target)
        if idx < len(nums) and nums[idx] == target:
            return idx
        else:
            return -1


sol = Solution()
print(sol.search([-1, 0, 3, 5, 9, 12], 9))

# Runtime: 260 ms, faster than 54.22%
