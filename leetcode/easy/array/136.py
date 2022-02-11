class Solution:
    def singleNumber(self, nums):
        s = nums[0]
        for num in nums[1:]:
            s ^= num
        return s




nums = [4, 1, 2, 1, 2]
sol = Solution()
print(sol.singleNumber(nums))
