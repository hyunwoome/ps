import heapq


class BinaryMaxHeap:
    # 인덱스 1부터 시작하는 배열 생성
    def __init__(self):
        self.items = [None]

    # 배열 길이 - 1
    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        cur = len(self)
        parent = cur // 2

        while parent:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = cur * 2
        right = cur * 2 + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)

    # 입력받은 값을 추가하고 루트로 올림
    def insert(self, num):
        self.items.append(num)
        self._percolate_up()

    # 루트 값과 맨 아래 값을 바꾸고 루트 값을 반환하며 제거
    # 바뀐 루트 값을 제자리에 놓기 위해 아래로 내림
    def extract(self):
        if len(self) < 1:
            return None
        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)
        return root


#
# class Solution:
#     def findKthLargest(self, nums, k):
#         maxheap = BinaryMaxHeap()
#         for num in nums:
#             maxheap.insert(num)
#
#         return [maxheap.extract() for _ in range(k)][k - 1]
#
#
# sol = Solution()
# print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))

class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

sol = Solution()
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))