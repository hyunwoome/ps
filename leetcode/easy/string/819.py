class Solution:
    def most_common_word(self, paragraph: str, banned):
        dic = {}
        banned = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower().split()

        for word in paragraph:
            if word not in banned:
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1
        return max(dic, key=dic.get)


p = "Bob hit a ball, the hit BALL flew far after it was hit."
b = ["hit"]
sol = Solution()
print(sol.most_common_word(p, b))
