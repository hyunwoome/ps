from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i, j = 0, 1
        n = len(s)  # 10
        res = []

        while i < n and j < n:
            if s[i] == s[j]:
                j += 1
            else:
                if j - i >= 3:
                    res.append([i, j - 1])
                i = j

        if j - i >= 3:
            res.append([i, j - 1])

        return res


sol = Solution()
_s = 'abbxxxxzzy'
print(sol.largeGroupPositions(_s))
