class Solution:
    def permute(self, nums):
        results = []
        prev_elements = []

        def dfs(elements):
            if not elements:
                results.append(prev_elements[:])
                return
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)

        return results


nums = [1, 2, 3]
sol = Solution()
print(sol.permute(nums))