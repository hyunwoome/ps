# 최소 힙
# 루트가 가장 작은 완전이진트리
# x가 0이면, 배열에서 가장 작은 값을 출력하고 그 값을 제거
import sys


class BinaryMinHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        cur = len(self)  # 들어온 값
        parent = cur // 2  # 들어온 값의 부모 노드

        while parent:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        smallest = cur
        left = cur * 2
        right = cur * 2 + 1

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != cur:
            self.items[cur], self.items[smallest] = self.items[smallest], self.items[cur]
            self._percolate_down(smallest)

    def insert(self, num):
        self.items.append(num)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return 0

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)
        return root


# 문제 풀이

def solution():
    N = int(sys.stdin.readline())
    min_heap = BinaryMinHeap()
    result = []
    for i in range(N):
        x = int(sys.stdin.readline())
        if x:
            min_heap.insert(x)
        else:
            result.append(str(min_heap.extract()))

    print('\n'.join(result))


solution()
