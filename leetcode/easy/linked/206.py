# 206. Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_all(self):
        while self:
            print(self.val, end=' ')
            self = self.next


class Solution:
    def reverse_list(self, head):
        cur = head  # 1. cur = 현재 노드를 가리키는 포인터
        prev = None  # 2. prev = 현재 노드의 이전을 가리키는 포인터

        # cur이 None이 아닐 때 까지
        while cur is not None:
            next = cur.next  # 3. next = 현재 노드의 다음을 가리키는 포인터
            cur.next = prev
            prev = cur
            cur = next

        return prev


# 3개의 포인터
# 1. cur = 현재 노드를 가리키는 포인터
# 2. prev = 현재 노드의 이전을 가리키는 포인터
# 3. next = 현재 노드의 다음을 가리키는 포인터


list5 = ListNode(5)
list4 = ListNode(4, list5)
list3 = ListNode(3, list4)
list2 = ListNode(2, list3)
list1 = ListNode(1, list2)
print(list1.print_all())

sol = Solution()
result = sol.reverse_list(list1)
result.print_all()  # 5 4 3 2 1
