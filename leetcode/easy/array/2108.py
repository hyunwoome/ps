from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def is_palindrome(word: str):
            if len(word) % 2 == 0:
                _start_word = word[:len(word) // 2]
                _end_word = word[len(word) // 2:][::-1]

                if _start_word == _end_word:
                    return True

            else:
                _start_word = word[:len(word) // 2]
                _end_word = word[len(word) // 2 + 1:][::-1]

                if _start_word == _end_word:
                    return True

            return False

        for word in words:
            if is_palindrome(word):
                return word

        return ""


words = ["abc", "car", "ada", "racecar", "cool"]
sol = Solution()
print(sol.firstPalindrome(words))
