import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_lst_by_bst(root, limit):
    if not root:
        return []

    lst = []
    q = collections.deque([root])

    while q:
        if len(lst) > limit:
            break

        node = q.popleft()
        if node:
            lst.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            lst.append(None)

    return lst


def sorted_array_to_bst(lst):
    if not lst:
        return None

    mid = len(lst) // 2

    node = TreeNode(lst[mid])
    node.left = sorted_array_to_bst(lst[:mid])
    node.right = sorted_array_to_bst(lst[mid + 1:])

    return node


def test_sorted_array_to_bst(lst):
    if not lst:
        return []
    root = sorted_array_to_bst(lst)
    return make_lst_by_bst(root, len(lst))


print(test_sorted_array_to_bst([10, -7, -3, -1, 0, 1, 4, 5, 7, 9]))
