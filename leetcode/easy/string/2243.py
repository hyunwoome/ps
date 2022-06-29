class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            lst = []
            for i in range(0, len(s), k):
                lst.append(s[i:i + k])

            temp = ''
            for num in lst:
                digits = [int(i) for i in num]
                temp += str(sum(digits))
            s = temp

        return s


sol = Solution()
_s = '11111222223'
_k = 3
print(sol.digitSum(_s, _k))
