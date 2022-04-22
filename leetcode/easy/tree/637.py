from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return [0]

        queue, result = deque([root]), []

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(sum(level) / len(level))

        return result


sol = Solution()

node2_2 = TreeNode(7)
node2_1 = TreeNode(15)
node1 = TreeNode(9)
node2 = TreeNode(20, node2_1, node2_2)
root_node = TreeNode(3, node1, node2)

print(sol.averageOfLevels(root_node))
