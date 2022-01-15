class Solution:
    def longest_palindrome(self, s):
        def is_palin(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1: j]

        p = ''
        for i in range(len(s)):
            p1 = is_palin(s, i, i + 1)
            p2 = is_palin(s, i, i)
            p = max([p, p1, p2], key=len)
        return p



s = 'babad'
sol = Solution()
print(sol.longest_palindrome(s))



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