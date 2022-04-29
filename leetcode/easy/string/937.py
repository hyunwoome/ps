from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 문자 > 숫자
        # 문자가 동일하면 식별자 순
        # 숫자는 입력순
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits


sol = Solution()
_logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
print(sol.reorderLogFiles(_logs))
