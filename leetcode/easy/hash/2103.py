from collections import defaultdict

class Solution:
    def countPoints(self, rings: str) -> int:
        rod_status = defaultdict(set)

        for i in range(0, len(rings), 2):
            rod_status[rings[i + 1]].add(rings[i])

        total = 0
        for r in rod_status:
            if len(rod_status[r]) == 3:
                total += 1

        return total


sol = Solution()
rings = 'B0B6G0R6R0R6G9'
print(sol.countPoints(rings))
