"""
* idea
1. 입력받는 numbers 배열은 오름차순 정렬되어 있으므로 이진 탐색을 사용할 수 있다.
2. 단순히 target을 찾는 것이 아닌, 덧셈하여 타겟을 만들 수 있는
배열의 두 숫자 인덱스를 반환해야 하므로, 반드시 한 번은 배열을 순회해야 한다. O(n log n)
3. 그러므로 for문을 한 번 사용해서 순회하고, 그 안에서 이진 탐색 적용
"""


class Solution:
    def twoSum(self, numbers, target):
        for i, v in enumerate(numbers):
            left, right = i + 1, len(numbers) - 1
            expected = target - v

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return i + 1, mid + 1


numbers = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(numbers, target))