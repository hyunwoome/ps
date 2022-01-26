import collections


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]  # 3
        if value is None:
            return
        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)
        return parent


def make_lst_by(root):
    if not root:
        return []

    lst = []
    q = collections.deque([root])

    while q:
        node = q.popleft()
        lst.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return lst


class Solution:
    def invertTree(self, lst):
        if not lst:
            return []

        def DFS(root):
            if root:
                root.left, root.right = DFS(root.right), DFS(root.left)
                return root

        root = make_tree_by(lst, 0)
        return make_lst_by(DFS(root))


sol = Solution()
print(sol.invertTree([4, 2, 7, 1, 3, 6, 9]))
