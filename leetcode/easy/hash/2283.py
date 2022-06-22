class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if num[i] != str(num.count(str(i))):
                return False
        return True


sol = Solution()
_num = "1210"
print(sol.digitCount(_num))
