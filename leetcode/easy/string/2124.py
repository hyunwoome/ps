class Solution:
    def checkString(self, s: str) -> bool:
        sorted_s = ''.join(sorted(s))

        return sorted_s == s


sol = Solution()
input_s = 'aaabbb'

print(sol.checkString(input_s))
