class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [None] * k  # 실제 리스트 공간 생성
        self.max_size = k  # 큐의 사이즈
        self.head = 0  # Head 포인터
        self.tail = 0  # Tail 포인터

    def enQueue(self, value: int) -> bool:
        # Tail이 None이면 큐가 차있는 것
        if self.data[self.tail] is None:
            self.data[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            return True
        else:
            return False

    def deQueue(self) -> bool:
        # Head가 None이면 큐가 비어있는 것
        if self.data[self.head] is None:
            return False
        else:
            self.data[self.head] = None
            self.head = (self.head + 1) % self.max_size
            return True

    def Front(self) -> int:
        if self.data[self.head] is None:
            return -1
        else:
            return self.data[self.head]

    def Rear(self) -> int:
        if self.data[self.tail - 1] is None:
            return -1
        else:
            return self.data[self.tail - 1]

    def isEmpty(self) -> bool:
        if self.head == self.tail and self.data[self.head] is None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.head == self.tail and self.data[self.head] is not None:
            return True
        else:
            return False


queue = MyCircularQueue(3)
print(queue.enQueue(1))
print(queue.enQueue(2))
print(queue.enQueue(3))
print(queue.enQueue(4))
print(queue.Rear())
