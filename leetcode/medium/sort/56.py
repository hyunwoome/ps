class Solution:
    def merge(self, intervals):
        intervals.sort()
        result = []
        for i in intervals:
            if not result or result[-1][1] < i[0]:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], i[1])

        return result


sol = Solution()
print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
