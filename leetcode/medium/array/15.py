class Solution:
    def three_sum(self, nums):
        answer = []
        nums.sort()
        n = len(nums)  # 6

        for i in range(n):  # 0 ~ 5
            j = i + 1
            k = n - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if not sum:  # 0
                    answer.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1

        return set(list(map(tuple, answer)))

nums = [-1, 0, 1, 2, -1, 4]
sol = Solution()
print(sol.three_sum(nums))
