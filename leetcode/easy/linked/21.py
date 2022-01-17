# 21. Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_all(self):
        while self:
            print(self.val, end=' ')
            self = self.next


# 풀이1. 반복
# class Solution:
#     def merge_two_lists(self, l1, l2):
#         answer = ListNode()  # [0| None]
#         cur = answer  # runner
#
#         # l1이나 l2 중에 None이 될 때까지 반복
#         while l1 and l2:
#             if l1.val > l2.val:
#                 cur.next = l2
#                 l2 = l2.next
#             else:
#                 cur.next = l1
#                 l1 = l1.next
#             cur = cur.next
#
#         # 한쪽이 None이 나와 종료되면 None이 아닌 나머지 노드를 마지막으로 가리키게 함
#         cur.next = l1 or l2
#
#         # answer노드의 next부터 실행
#         return answer.next


# 총 4개의 ListNode 필요
# 1. answer : tmp를 가리켜 정렬된 노드들을 출력하는 ListNode (0번 노드)
# 2. cur : 노드들을 따라가면서 정렬하는 ListNode
# 3. list1 : 1번 리스트
# 4. list2 : 2번 리스트


# # list1
# # ListNode1(1, ListNode2) - ListNode2(2, ListNode3) - ListNode3(4, None)
# list1_3 = ListNode(4)  # None
# list1_2 = ListNode(2, list1_3)
# list1_1 = ListNode(1, list1_2)  # [1| list1_2] -> [2| list1_3] -> [3| None]
# print(list1_1.print_all())  # 1 2 4 None
#
# # list2
# # ListNode1(1, ListNode2) - ListNode2(3, ListNode3) - ListNode3(4, None)
# list2_3 = ListNode(4)
# list2_2 = ListNode(3, list2_3)
# list2_1 = ListNode(1, list2_2)
# print(list2_1.print_all())  # 1 3 4 None
#
# # cur = [0, 1, 1, 2, 3, 4, 4]
#
# sol = Solution()
# result = sol.merge_two_lists(list1_1, list2_1)
# result.print_all()  # 1 1 2 3 4 4


# 풀이2. 재귀
class Solution:
    def merge_two_lists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2

        if l1.val < l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)
        else:
            l2.next = self.merge_two_lists(l1, l2.next)
            return l2


# list1
# ListNode1(1, ListNode2) - ListNode2(2, ListNode3) - ListNode3(4, None)
list1_3 = ListNode(4)  # None
list1_2 = ListNode(2, list1_3)
list1_1 = ListNode(1, list1_2)  # [1| list1_2] -> [2| list1_3] -> [3| None]
print(list1_1.print_all())  # 1 2 4 None

# list2
# ListNode1(1, ListNode2) - ListNode2(3, ListNode3) - ListNode3(4, None)
list2_3 = ListNode(4)
list2_2 = ListNode(3, list2_3)
list2_1 = ListNode(1, list2_2)
print(list2_1.print_all())  # 1 3 4 None

sol = Solution()
result = sol.merge_two_lists(list1_1, list2_1)
result.print_all()  # 1 1 2 3 4 4