class Solution:
    def bitwiseComplement(self, n: int) -> int:
        to_bin = bin(n)[2:]
        convert = '0b'
        for i in to_bin:
            if i == '0':
                convert += '1'
            else:
                convert += '0'

        return int(convert, 2)


sol = Solution()
_n = 5
print(sol.bitwiseComplement(_n))
