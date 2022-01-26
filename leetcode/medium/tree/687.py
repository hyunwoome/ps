class TreeNode:
    def __init__(self, val, left=None, right=None):
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
    answer = 0

    def longestUnivaluePath(self, root):
        root = make_tree_by(root, 0)
        self.DFS(root)
        return self.answer

    def DFS(self, node):
        if not node:
            return 0

        left = self.DFS(node.left)
        right = self.DFS(node.right)

        if node.left and node.left.val == node.val:
            left += 1
        else:
            left = 0
        if node.right and node.right.val == node.val:
            right += 1
        else:
            right = 0

        self.answer = max(self.answer, left + right)
        return max(left, right)


root = [5, 4, 5, 1, 1, 5]
sol = Solution()
print(sol.longestUnivaluePath(root))
