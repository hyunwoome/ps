class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        result = 0

        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
                result += 1
            else:
                num2 -= num1
                result += 1

        return result



sol = Solution()
input_num1 = 2
input_num2 = 3
print(sol.countOperations(input_num1, input_num2))