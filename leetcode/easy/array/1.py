# 풀이 1. 브루트 포스
# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

#풀이 2. 해시를 이용한 풀이
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i, v in enumerate(nums):
            dict[v] = i

        for i, v in enumerate(nums):
            if target - v in dict and i != dict[target - v]:
                return [i, dict[target - v]]



nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))
