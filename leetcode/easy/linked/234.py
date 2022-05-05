from typing import Optional
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        q = deque()

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True


sol = Solution()
node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
print(sol.isPalindrome(node1))
