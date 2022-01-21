class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0
        answer = 0
        used = {}

        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                answer = max(answer, i - start + 1)

            used[s[i]] = i

        return answer


s = 'abcabcbb'
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
