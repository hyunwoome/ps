class Solution:
    def greatestLetter(self, s: str) -> str:
        """
        해당 문자가 대문자이고, 그 문자를 소문자로 변경 후
        s에 포함되어 있다면, 문자열에 대문자와 소문자가 있다는 뜻
        그래서 빈 list에 담고 가장 많은 알파벳을 반환
        만약 없다면 빈 문자열('')을 반환
        """
        arr = []

        for i in s:
            if ord(i) < 91 and (chr(ord(i) + 32) in s):
                arr.append(i)

        return max(arr) if len(arr) != 0 else ''


sol = Solution()
_s = "lEeTcOdE"
print(sol.greatestLetter(_s))
