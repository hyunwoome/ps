class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]  # 1
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)  # 2 # 4
        parent.right = make_tree_by(lst, 2 * idx + 2)  # 3 # 5
        return parent


class Solution:
    longest = 0

    def diameterOfBinaryTree(self, root):
        root = make_tree_by(root, 0)
        level = 0
        self.DFS(root, level)
        return self.longest

    def DFS(self, node, level):
        if not node:
            return 0

        left = self.DFS(node.left, level + 1)
        right = self.DFS(node.right, level + 1)

        self.longest = max(self.longest, left + right)
        return max(left, right) + 1


sol = Solution()
print(sol.diameterOfBinaryTree([1, 2, 3, 4, 5]))
