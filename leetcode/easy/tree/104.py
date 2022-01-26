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


def maxDepth(lst):
    root = make_tree_by(lst, 0)
    if not root:
        return 0

    q = collections.deque([root])  # 3
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            # cur = 3
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    return depth


print(maxDepth([3, 9, 20, None, None, 15, 17]))
