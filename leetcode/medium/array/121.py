import sys


class Solution:
    def maxProfit(self, prices):
        profit = 0
        min_price = sys.maxsize

        for i in prices:
            min_price = min(min_price, i)
            profit = max(profit, i - min_price)
        return profit


p = [7, 1, 5, 3, 6, 4]
sol = Solution()
print(sol.maxProfit(p))
