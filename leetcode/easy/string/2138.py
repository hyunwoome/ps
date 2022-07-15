from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for i in range(0, len(s), k):
            words = s[i:i + k]
            result.append(words + (k - len(words)) * fill)
        return result


sol = Solution()
_s = 'abcdefghi'
_k = 3
_fill = 'x'
print(sol.divideString(_s, _k, _fill))
