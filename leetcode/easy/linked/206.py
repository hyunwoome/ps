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
        cur = head
        prev = None

        # cur이 None이 아닐 때 까지
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev


list5 = ListNode(5)
list4 = ListNode(4, list5)
list3 = ListNode(3, list4)
list2 = ListNode(2, list3)
list1 = ListNode(1, list2)
print(list1.print_all())

sol = Solution()
result = sol.reverse_list(list1)
result.print_all()  # 5 4 3 2 1
