from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


sol = Solution()

list1_3 = ListNode(4)
list1_2 = ListNode(2, list1_3)
list1_1 = ListNode(1, list1_2)

list2_3 = ListNode(4)
list2_2 = ListNode(3, list2_3)
list2_1 = ListNode(1, list2_2)

print(sol.mergeTwoLists(list1_1, list2_1))
