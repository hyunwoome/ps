from typing import List


class Solution:
    def most_words_found(self, sentences: List[str]) -> int:
        return max(len(word.split()) for word in sentences)


sol = Solution()
print(sol.most_words_found(["please wait",
                            "continue to fight",
                            "continue to win"]))
