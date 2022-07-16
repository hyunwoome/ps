class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        result = 0

        str_num = str(num)
        # 0 ~ (6 - 2)
        for i in range(len(str_num) + 1 - k):
            sub_word = int(str_num[i:i + k])
            if sub_word != 0 and num % sub_word == 0:
                result += 1

        return result


sol = Solution()
_num = 430043  # 6 - 1
_k = 2
print(sol.divisorSubstrings(_num, _k))
