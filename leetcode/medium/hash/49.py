class Solution:
    def group_anagrams(self, strs):
        answer = []
        dic = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word] = [word]
            else:
                dic[sorted_word].append(word)

        for v in dic.values():
            answer.append(v)
        return answer




arr = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
sol = Solution()
print(sol.group_anagrams(arr))
