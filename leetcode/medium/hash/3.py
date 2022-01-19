class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        문제: 중복된 문자없이 가장 긴 문자열을 반환하라
            1. 포인터 두 개를 이용해 슬라이딩 윈도우
            2. used: 문자와 인덱스를 저장할 딕셔너리
            3. start: 시작 포인터, index: 마지막 포인터
            4. max_length: 가장 긴 길이의 문자열을 갱신하는 변수
        """
        used = {}
        start = 0
        max_length = 0

        for index, char in enumerate(s):
            """
            이미 문자열이 들어있어 중복된 경우엔
            """
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index

        return max_length


s = 'pwwkew'
sol = Solution()
print(sol.lengthOfLongestSubstring(s))

"""
max_length: 3
used : {p:0, w:5, k:3, e:4,}
p w w k e w
0 1 2 3 4 5
      s
          i 
"""

