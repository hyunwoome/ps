class Solution:
    def permute(self, nums):
        results = []
        prev_elements = []

        def dfs(elements):
            # 종료조건
            if len(elements) == 0:
                results.append(prev_elements[:])
                return

            # for문을 돌리며 각 요소마다 dfs() 실행
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()  # dfs()가 리턴된 후 실행됨

        dfs(nums)
        return results


nums = [1, 2, 3]
sol = Solution()
print(sol.permute(nums))
