class Solution:
    def countAsterisks(self, s: str) -> int:
        number_of_asteriksks = 0
        flag = False

        for i in s:
            if i == '|' and not flag:
                flag = True
            elif i == '|' and flag:
                flag = False
            elif i == '*' and not flag:
                number_of_asteriksks += 1

        return number_of_asteriksks


sol = Solution()
_s = 'yo|uar|e**|b|e***au|tifu|l'
print(sol.countAsterisks(_s))
