# 1. 파이썬 문자열 기능 사용
# class Solution:
#     def is_palindrome(self, s):
#         remove_space = s.replace(' ', '')  # 1. 공백 제거
#         remove_non_alpha = ''.join(filter(str.isalnum, remove_space)) # 2. 특수문자 제거
#         to_lowercase = remove_non_alpha.lower()  # 3. 소문자로 변경
#         return to_lowercase == to_lowercase[::-1]
#
# s = 'A man, a plan, a canal: Panama'
# sol = Solution()
# print(sol.is_palindrome(s))
# Runtime: 70ms, faster than 27.07%



# 2. 정규식을 사용한 문제 풀이
import re


class Solution():
    def is_palindrome(self, s):
        s = s.lower()  # 소문자 변경
        s = re.sub('[^a-z0-9]', '', s)  # a-z, 0-9까지를 제외한 나머지 문자열은 제거
        return s == s[::-1]


s = 'A man, a plan, a canal: Panama'
sol = Solution()
print(sol.is_palindrome(s))
# Runtime: 36 ms, faster than 96.36%