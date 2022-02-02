class BinaryMinHeap:
    # 0번 인덱스가 None인 item 배열 생성
    def __init__(self):
        self.item = [None]

    # item 배열 출력
    def print_item(self):
        print(self.item)

    # 기존 len메서드 재정의 (overriding)
    def __len__(self):
        return len(self.item) - 1

    """
    원소를 힙에 삽입했을 때, 제자리로 찾아가게 하는 메서드
    1. 삽입한 원소의 현재 위치(cur, 맨 뒤)에서 반 나눈 인덱스의 값을 parent로 보고,
    2. cur과 parent를 비교하여 더 낮은 값을 위로 올려보냄(swap)
    3. parent를 다 비교할 때 까지 과정을 반복
    """

    def _percolate_up(self):
        cur = len(self)
        parent = cur // 2

        while parent > 0:
            if self.item[cur] < self.item[parent]:
                self.item[cur], self.item[parent] = self.item[parent], self.item[cur]

            cur = parent
            parent = cur // 2

    """
    루트 노드(가장 최소값)와 맨 아래 노드를 스왑시킨 후에(extract()) 
    루트 노드가 밑으로 내려가면서 제자리를 찾아가게 해주는 메서드
    1. 현재 루트 노드를 가장 작은 값으로 가정하고 루트 노드 기준으로 왼쪽과 오른쪽 노드와 비교
    2. 각각을 비교해서 현재 노드가 더 크다면 아래로 내려가야 하므로 스왑시켜줌
    """

    def _percolate_down(self, cur):
        smallest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.item[left] < self.item[smallest]:
            smallest = left

        if right <= len(self) and self.item[right] < self.item[smallest]:
            smallest = right

        if smallest != cur:
            self.item[cur], self.item[smallest] = self.item[smallest], self.item[cur]
            self._percolate_down(smallest)

    # 원소를 item 배열에 추가하고 제자리를 찾게 해주는 _percolate_up()메서드를 호출한다.
    def insert(self, k):
        self.item.append(k)
        self._percolate_up()

    # 루트 노드의 원소를 제거할 때 루트 노드와 맨 아래 노드를 스왑하게 되고,
    # 스왑한 노드를 아래로 내리면서 제자리를 찾게 해주는 _percolate_down(1)을 호출한다.
    def extract(self):
        if len(self) < 1:
            return None

        root = self.item[1]
        self.item[1] = self.item[-1]
        self.item.pop()
        self._percolate_down(1)
        return root


# 최소힙 객체 생성
min_heap = BinaryMinHeap()

# 최소힙에 원소 삽입
min_heap.insert(100)
min_heap.insert(10)
min_heap.insert(15)
min_heap.insert(45)
min_heap.insert(30)
min_heap.insert(40)
min_heap.insert(50)
min_heap.print_item()  # [None, 10, 30, 15, 100, 45, 40, 50]

min_heap.insert(20)
min_heap.print_item()  # [None, 10, 20, 15, 30, 45, 40, 50, 100]

#  최소값 추출
print(min_heap.extract())  # 10
print(min_heap.extract())  # 15
print(min_heap.extract())  # 20
print(min_heap.extract())  # 30
print(min_heap.extract())  # 40
print(min_heap.extract())  # 45
print(min_heap.extract())  # 50

min_heap.print_item()  # [None, 100]

"""
삽입 시간복잡도: O(log(N))
추출 시간복잡도: O(log(N))
"""