class Solution:
    def array_pair_sum(self, nums):
        answer = 0
        nums.sort()
        length = len(nums) // 2  # 2
        i = 0
        while length:
            answer += nums[i]
            i += 2
            length -= 1
        return answer


nums = [6, 2, 6, 5, 1, 2]
sol = Solution()
print(sol.array_pair_sum(nums))
