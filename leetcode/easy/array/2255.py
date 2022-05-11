from typing import List


class Solution:
    """
    Title: LeetCode 2255. Count Prefiexes
    Author: Hyunwoo Lim
    Date: 2022.05.11
    """
    def countPrefixes(self, words: List[str], s: str) -> int:
        result = 0

        for i in words:
            if s.startswith(i):
                result += 1

        return result


sol = Solution()
_words = ["a", "b", "c", "ab", "bc", "abc"]
_s = "abc"
print(sol.countPrefixes(_words, _s))

