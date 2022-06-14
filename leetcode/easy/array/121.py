from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            # 매수와 매도의 차
            current_profit = prices[sell] - prices[buy]

            # 이득일 경우
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, current_profit)
            else:
                buy = sell

            sell += 1

        return max_profit


sol = Solution()
_prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(_prices))
