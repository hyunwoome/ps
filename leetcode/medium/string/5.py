class Solution:
    def longest_palindrome(self, s):

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for index in range(len(s) - 1):
            result = max(result,
                         expand(index, index + 1),  # 0 ~ 1 (짝수개)
                         expand(index, index + 2),  # 0 ~ 2 (홀수개)
                         key=len)
        return result


sol = Solution()
assert sol.longest_palindrome('babad') == 'bab'
assert sol.longest_palindrome('cbbd') == 'bb'

# 시간초과
# class Solution:
#     def longest_palindrome(self, s):
#         if len(s) == 1:
#             return ''.join(s)
#
#         def is_pal(normal, reverse):
#             reverse = reverse[::-1]
#             return normal == reverse
#
#         answer = []
#         for i, v in list(enumerate(s)):
#             j = 1
#             while j < len(s):
#                 tmp = ''
#                 for idx in range(i, j + 1):
#                     tmp += s[idx]
#
#                 if is_pal(tmp, tmp):
#                     answer.append(tmp)
#                 j += 1
#
#         return max(answer, key=len)
#
#
# s = 'civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'
# sol = Solution()
# print(sol.longest_palindrome(s))
