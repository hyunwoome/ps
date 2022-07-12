from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        time_max = 0

        for i in range(n):
            if i == 0:
                time_i = releaseTimes[i]
            else:
                time_i = releaseTimes[i] - releaseTimes[i - 1]

            if time_i > time_max:
                time_max = time_i
                result = keysPressed[i]

            if time_i == time_max and result < keysPressed[i]:
                result = keysPressed[i]

        return result


sol = Solution()
_releaseTimes = [9, 29, 49, 50]
_keysPressed = 'cbcd'
print(sol.slowestKey(_releaseTimes, _keysPressed))
