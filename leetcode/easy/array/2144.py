from typing import List
# from collections import deque
#
#
# class Solution:
#     def minimumCost(self, cost: List[int]) -> int:
#         result = 0
#         sorted_cost = deque(sorted(cost, reverse=True))
#
#         tmp = 0
#
#         while sorted_cost:
#             if tmp != 2:
#                 result += sorted_cost.popleft()
#                 tmp += 1
#             else:
#                 sorted_cost.popleft()
#                 tmp = 0
#
#         return result

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        print(cost[2::3])
        print(cost)
        return sum(cost) - sum(cost[2::3])


sol = Solution()
_cost = [6,5,7,9,2,2]
print(sol.minimumCost(_cost))
