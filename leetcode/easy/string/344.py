# 1. 투포인터 스왑
# class Solution:
#     def reverse_string(self, s):
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         l, r = 0, len(s) -1
#         while l < r:
#             s[l], s[r] = s[r], s[l]
#             l += 1
#             r -=1
#
#
# s = ["h", "e", "l", "l", "o"]
# sol = Solution()
# sol.reverse_string(s)
# Runtime: 258 ms, faster than 29.84%

# 2. reverse이용
class Solution:
    def reverse_string(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


s = ["h", "e", "l", "l", "o"]
sol = Solution()
sol.reverse_string(s)
# Runtime: 172 ms, faster than 100.00%