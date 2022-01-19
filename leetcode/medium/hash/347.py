class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        answer = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        arr = list(sorted_d.keys())
        for i in range(0, k):
            answer.append(arr[i])
        return answer



nums = [3, 0, 1, 0]
k = 1
sol = Solution()
print(sol.topKFrequent(nums, k))
