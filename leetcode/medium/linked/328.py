# 328. Odd Even Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_all(self):
        while self:
            print(self.val, end=' ')
            self = self.next


class Solution:
    def odd_even_list(self, head):
        odd = head  # 홀수
        even = head.next  # 짝수
        even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = even_head
        return head


list5 = ListNode(5)
list4 = ListNode(4, list5)
list3 = ListNode(3, list4)
list2 = ListNode(2, list3)
list1 = ListNode(1, list2)
print(list1.print_all())  # 1, 2, 3, 4, 5, None

sol = Solution()
result = sol.odd_even_list(list1)
result.print_all()  # 1, 3, 5, 2, 4
