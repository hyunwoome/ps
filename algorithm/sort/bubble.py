def bubble_sort(lst):
    for i in range(len(lst) - 1):
        wall = len(lst) - 1 - i
        for j in range(wall):
            next_j = j + 1
            if lst[j] > lst[next_j]:
                lst[j], lst[next_j] = lst[next_j], lst[j]

    return lst


print(bubble_sort([4, 6, 2, 9, 1]))  # [1, 2, 4, 6, 9]
