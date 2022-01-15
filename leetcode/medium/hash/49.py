class Solution:
    def group_anagrams(self, strs):
        answer = []
        hash_map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hash_map:
                hash_map[sorted_word] = [word]
            else:
                hash_map[sorted_word].append(word)

        for k, v in hash_map.items():
            answer.append(v)
        return answer

# aet aet ant aet ant abt
# eat
arr = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
sol = Solution()
print(sol.group_anagrams(arr))
