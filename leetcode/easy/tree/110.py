class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is None:
            return
        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)
        return parent


class Solution:
    def isBalanced(self, root):
        root = make_tree_by(root, 0)
        return self.DFS(root) != -1

    def DFS(self, dfs_root):
        if not dfs_root:
            return 0

        left = self.DFS(dfs_root.left)
        right = self.DFS(dfs_root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1


sol = Solution()
print(sol.isBalanced([3, 9, 20, None, None, 15, 7]))
