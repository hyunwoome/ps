# def bubble_sort(lst):
#     for i in range(len(lst) - 1):
#         wall = len(lst) - 1 - i
#         for j in range(wall):
#             next_j = j + 1
#             if lst[j] > lst[next_j]:
#                 lst[j], lst[next_j] = lst[next_j], lst[j]
#
#     return lst
#
#
# print(bubble_sort([4, 6, 2, 9, 1]))  # [1, 2, 4, 6, 9]

# def bubble_sort(lst):
#     # lst만큼 라운드 진행
#     for _ in lst:
#         i = 0
#         j = 1
#         for _ in range(len(lst) - 1):
#             if lst[i] > lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#             i += 1
#             j += 1
#
#     return lst
#
#
# print(bubble_sort([4, 6, 2, 9, 1]))
# # [1, 2, 4, 6, 9]

def improved_bubble_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


print(improved_bubble_sort([4, 6, 2, 9, 1]))
# [1, 2, 4, 6, 9]
