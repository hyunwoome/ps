class Solution:
    def letterCombinations(self, digits):
        dic = {'2': 'abc', '3': 'def',
               '4': 'ghi', '5': 'jkl', '6': 'mno',
               '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return list(dic[digits[0]])








digits = '23'
sol = Solution()
print(sol.letterCombinations(digits))
