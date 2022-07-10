from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        result = float('inf')
        d = Counter(s)
        d1 = Counter(target)

        for i in d1.keys():  # c, o, d, e
            if i not in d:
                return 0
            x = d[i] // d1[i]
            result = min(result, x)

        return result



sol = Solution()
_s = 'ilovecodingonleetcode'
_target = 'code'
print(sol.rearrangeCharacters(_s, _target))
