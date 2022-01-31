class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_all(self):
        while self:
            print(self.val, end=' ')
            self = self.next


"""
# 문제
단일 연결 리스트의 head가 주어지고, 삽입 정렬을 사용해서 정렬한 후
정렬된 리스트의 head를 반환하시오.
"""


class Solution:
    def insertionSortList(self, head):
        pass
# [4, 2, 1, 3]
# cur = parent = ListNode(None)
# while head:
#     while cur.next and cur.next.val < head.val:
#         cur = cur.next
#
#     cur.next, head.next, head = head, cur.next, head.next
#
# cur = parent
# return cur.next


list4 = ListNode(3)
list3 = ListNode(1, list4)
list2 = ListNode(2, list3)
list1 = ListNode(4, list2)

sol = Solution()
result = sol.insertionSortList(list1)
result.print_all()
