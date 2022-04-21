from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val


right_node = TreeNode(1)
left_node = TreeNode(3)
root_node = TreeNode(5, left_node, right_node)

sol = Solution()
print(sol.checkTree(root_node))
