class Solution:
    def numJewelsInStones(self, jewels, stones):
        dict = {}
        answer = 0
        for i in range(len(stones)):
            if stones[i] in dict:
                dict[stones[i]] += 1
            else:
                dict[stones[i]] = 1

        for i in jewels:
            for k, v in dict.items():
                if i is k:
                    answer += v
        return answer

jewels = 'aA'
stones = 'aAAbbbb'
sol = Solution()
print(sol.numJewelsInStones(jewels, stones))
