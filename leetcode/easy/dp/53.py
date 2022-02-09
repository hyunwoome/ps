class Solution:
    def maxSubArray(self, nums):
        dp = [nums[0]]
        for i in range(1, len(nums)):
            # dp테이블에 현재까지 더한 값들을 기록한다.
            # dp테이블에 현재까지 더한 값이 0 이상일 때, 현재까지 더한 값 + nums의 해당 인덱스값
            # dp테이블에 현재까지 더한 값이 0 이하일 때, 기존 nums의 해당 인덱스값을 삽입
            if dp[i - 1] >= 0:
                dp.append(nums[i] + dp[i - 1])
            else:
                dp.append(nums[i])

        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
print(sol.maxSubArray(nums))
# Runtime: 720 ms, faster than 88.10%
