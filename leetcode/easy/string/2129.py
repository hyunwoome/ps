class Solution:
    def capitalizeTitle(self, title: str) -> str:
        """
        단어의 길이가 2이하면 소문자로 변환
        단어의 길이가 2이상이면
        - 첫 번째 글자 -> 대문자
        - 나머지 글자 -> 소문자
        """
        result = []

        lowercase_word = title.lower()
        word_list = lowercase_word.split(' ')

        for word in word_list:
            if len(word) < 3:
                result.append(word)
            else:
                uppercase = word[0].upper() + word[1:]
                result.append(uppercase)

        return ' '.join(result)


sol = Solution()
_title = "capiTalIze tHe titLe"
print(sol.capitalizeTitle(_title))
