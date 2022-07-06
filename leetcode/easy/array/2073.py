from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0

        while tickets[k] != 0:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    break

                if tickets[i] > 0:
                    tickets[i] -= 1
                    count += 1
                else:
                    continue

        return count


sol = Solution()
_tickets = [5, 1, 1, 1]
_k = 0
print(sol.timeRequiredToBuy(_tickets, _k))
