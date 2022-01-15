# 조건
# 1. 문자 > 숫자
# 2. 숫자는 순서대로

class Solution:
    def reorder_log_files(self, logs):
        letter = []
        digits = []
        for log in logs:
            split_log = log.split(' ', 1)
            if split_log[1][0].isdigit():
                digits.append(log)
            else:
                letter.append([split_log[1], split_log[0]])
        letter.sort()

        join_letter = []
        for let in letter:
            order = let[1] + ' ' + let[0]
            join_letter.append(order)

        return join_letter + digits

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
sol = Solution()
print(sol.reorder_log_files(logs))
