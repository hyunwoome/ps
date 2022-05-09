from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(None)
        root = prev
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next

        return root.next


sol = Solution()
list4 = ListNode(4)
list3 = ListNode(3, list4)
list2 = ListNode(2, list3)
list1 = ListNode(1, list2)

print(sol.swapPairs(list1))
