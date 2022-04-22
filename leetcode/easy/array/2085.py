from typing import List
from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = Counter(words1 + words2)
        return len([word for word in count if count[word] == 2 and word in words1 and word in words2])


sol = Solution()
words1 = ["a", "ab"]
words2 = ["a", "a", "a", "ab"]
print(sol.countWords(words1, words2))
