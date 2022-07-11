from typing import List
from collections import defaultdict


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic = defaultdict(int)
        for i in words:
            for j in i:
                dic[j] += 1

        for k, v in dic.items():
            if v % len(words):
                return False

        return True


sol = Solution()
_words = ["abc", "aabc", "bc"]
print(sol.makeEqual(_words))
