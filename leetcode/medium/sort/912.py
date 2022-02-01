class Solution:
    def sortArray(self, nums):
        def merge(left, right):
            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        L = nums[:mid]
        R = nums[mid:]
        return merge(self.sortArray(L), self.sortArray(R))


sol = Solution()
print(sol.sortArray([5, 2, 3, 1]))
