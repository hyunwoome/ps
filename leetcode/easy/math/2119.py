class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reverse_num = int(str(num)[::-1])
        re_reverse_num = int(str(reverse_num)[::-1])
        return num == re_reverse_num


sol = Solution()
input_num = 0

print(sol.isSameAfterReversals(input_num))
