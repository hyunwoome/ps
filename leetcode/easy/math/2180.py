class Solution:
    def countEven(self, num: int) -> int:
        # num까지 자릿수의 합이 짝수인 수의 개수를 반환
        count = 0

        for i in range(2, num + 1):
            num_sum = sum(map(int, str(i)))
            if num_sum % 2 == 0:
                count += 1

        return count


sol = Solution()
_num = 30
print(sol.countEven(_num))
