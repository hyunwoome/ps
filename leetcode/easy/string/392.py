class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        start = 0
        for i in range(len(t)):
            if t[i] == s[start]:
                start += 1
                if start == len(s):
                    return True

        return False


sol = Solution()
_s = 'abc'
_t = 'ahbgdc'
print(sol.isSubsequence(_s, _t))
