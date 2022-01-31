# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_all(self):
        while self:
            print(self.val, end=' ')
            self = self.next


class Solution:
    def sortList(self, head):
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next

        return head


sol = Solution()
list5 = ListNode(0)
list4 = ListNode(4, list5)
list3 = ListNode(3, list4)
list2 = ListNode(5, list3)
list1 = ListNode(-1, list2)
result = sol.sortList(list1)
result.print_all()