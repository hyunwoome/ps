import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


def make_lst_by_bst(root, limit):
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


"""
1. Serialize : 논리적인 데이터 구조를 물리적 형태로 바꿔주는 작업
2. Deserialize : 물리적 형태의 데이터 구조를 논리적인 데이터 구조로 바꿔주는 작업 
"""


class Codec:

    def serialize(self, root):
        if not root:
            return []
        tree_root = make_tree_by(root, 0)

        # 1번 인덱스부터 루트노드
        result = ['#']
        q = collections.deque([tree_root])

        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data, root):
        if data == '# #':
            return None

        nodes = data.split()  # ['#', '1', '2'....]
        tree_root = TreeNode(int(nodes[1]))
        q = collections.deque([tree_root])
        index = 2

        while q:
            node = q.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1

            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1

        return make_lst_by_bst(tree_root, len(root) - 1)


ser = Codec()
print(ser.serialize([1, 2, 3, None, None, 4, 5]))
print(ser.deserialize('# 1 2 3 # # 4 5 # # # #', [1, 2, 3, None, None, 4, 5]))
