import sys


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        서브스트링이 반드시 세글자
        세글자 모두 하나의 글자로만 이루어져야 함
        """
        tmp = -sys.maxsize
        for i in range(len(num) - 2):
            first = num[i]
            second = num[i + 1]
            third = num[i + 2]

            if first == second == third:
                tmp = max(int(first + second + third), tmp)

        if tmp == 0:
            return '000'
        elif tmp == -sys.maxsize:
            return ''

        return str(tmp)


sol = Solution()
_num = '2300019'
print(sol.largestGoodInteger(_num))
