class BinaryMinHeap:
    def __init__(self):
        self.item = [None]

    def __len__(self):
        return len(self.item) - 1

    def _percolate_up(self):
        cur = len(self)
        parent = cur // 2

        while parent:
            if self.item[cur] < self.item[parent]:
                self.item[cur], self.item[parent] = self.item[parent], self.item[cur]

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        smallest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.item[left] < self.item[smallest]:
            smallest = left

        if right <= len(self) and self.item[right] < self.item[smallest]:
            smallest = right

        if smallest != cur:
            self.item[smallest], self.item[cur] = self.item[cur], self.item[smallest]
            self._percolate_down(smallest)

    def insert(self, k):
        self.item.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.item[1]
        self.item[1] = self.item[-1]
        self.item.pop()
        self._percolate_down(1)
        return root


class Solution:
    def sortArray(self, nums):
        min_heap = BinaryMinHeap()
        for i in nums:
            min_heap.insert(i)

        return [min_heap.extract() for _ in range(len(nums))]

sol = Solution()
print(sol.sortArray([5, 2, 3, 1]))