class Solution:
    def convertTime(self, current: str, correct: str) -> int:

        current = current.split(':')
        correct = correct.split(':')

        for i in range(len(current)):
            current[i] = int(current[i])
            correct[i] = int(correct[i])

        # 1시간을 60분으로 전환
        remain = ((correct[0] * 60) + correct[1]) - ((current[0] * 60) + current[1])

        result = 0

        while remain != 0:
            if remain >= 60:
                result += 1
                remain -= 60

            elif remain >= 15:
                result += 1
                remain -= 15

            elif remain >= 5:
                result += 1
                remain -= 5

            elif remain >= 1:
                result += 1
                remain -= 1

        return result


sol = Solution()
_current = "02:30"
_correct = "04:35"
print(sol.convertTime(_current, _correct))
