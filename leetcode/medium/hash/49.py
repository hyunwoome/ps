from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())


sol = Solution()
_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(_strs))

