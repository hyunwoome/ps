class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = sorted([i for i in str(num)])
        num_1 = num_list[0] + num_list[2]
        num_2 = num_list[1] + num_list[3]
        return int(num_1) + int(num_2)


sol = Solution()
print(sol.minimumSum(4009))