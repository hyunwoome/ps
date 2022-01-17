class Solution:
    def daily_temperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer


t = [73, 74, 75, 71, 69, 72, 76, 73]
sol = Solution()
print(sol.daily_temperatures(t))
