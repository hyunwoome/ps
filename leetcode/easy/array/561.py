class Solution:
    def array_pair_sum(self, nums):
        return sum(sorted(nums)[::2])


nums = [6, 2, 6, 5, 1, 2]
sol = Solution()
print(sol.array_pair_sum(nums))
