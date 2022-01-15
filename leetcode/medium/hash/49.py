class Solution:
    def group_anagrams(self, strs):
        answer = []
        hash_map = {}

        for word in strs:
            # 각 단어들 정렬
            sorted_word = ''.join(sorted(word))

            # 빈 딕셔너리에 정렬된 단어가 없으면
            # key(정렬된 단어) : [value(단어)]
            if sorted_word not in hash_map:
                hash_map[sorted_word] = [word]
            else:
                # 빈 딕셔너리에 이미 정렬된 단어가 있으면,
                # key(정렬된 단어) : [value]에 추가
                hash_map[sorted_word].append(word)

        # 딕셔너리에서 값만 추출하여 추가
        for k, v in hash_map.items():
            answer.append(v)
        return answer


# aet aet ant aet ant abt
arr = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
sol = Solution()
print(sol.group_anagrams(arr))
