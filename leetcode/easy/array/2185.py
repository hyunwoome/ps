from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pref_len = len(pref)  # 2
        count = 0

        for word in words:
            sep_word = word[:pref_len]
            if pref == sep_word:
                count += 1

        return count


sol = Solution()

input_words = ["pay", "attention", "practice", "attend"]
input_pref = "at"
print(sol.prefixCount(input_words, input_pref))
