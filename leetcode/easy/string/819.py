import re
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[\W]', ' ', paragraph)
                 .lower().split()
                 if word not in banned]

        counts = Counter(words)
        return counts.most_common(1)[0][0]


sol = Solution()
_paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
_banned = ["hit"]
print(sol.mostCommonWord(_paragraph, _banned))

