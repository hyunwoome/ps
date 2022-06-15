import math


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        total = len(s)
        cnt = s.count(letter)
        return math.floor((cnt / total) * 100)


sol = Solution()
_s = "foobar"
_letter = "o"
print(sol.percentageLetter(_s, _letter))
