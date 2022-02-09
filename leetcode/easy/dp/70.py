class Solution:
    def climbStairs(self, n):
        # Tabulation
        dp = [0] * 100
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


n = 2
sol = Solution()
print(sol.climbStairs(n))
