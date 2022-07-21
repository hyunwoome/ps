class Solution:
    def minOperations(self, s: str) -> int:
        c1 = 0
        c2 = 0
        one = '1'
        zero = '0'

        for i in range(len(s)):
            if s[i] != one:
                c1 += 1
            else:
                c2 += 1

            one, zero = zero, one

        return min(c1, c2)


sol = Solution()
_s = "0100"
print(sol.minOperations(_s))
