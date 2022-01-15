class Solution:
    def array_pair_sum(self, nums):
        answer = 0
        # 배열 오름차순으로 정렬
        sorted_arr = sorted(nums)  # [1, 2, 3, 4]
        length = len(sorted_arr) // 2  # 2
        i = 0
        while length:
            answer += sorted_arr[i]
            i += 2
            length -= 1
        return answer


nums = [6, 2, 6, 5, 1, 2]
sol = Solution()
print(sol.array_pair_sum(nums))
