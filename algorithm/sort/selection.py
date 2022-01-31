def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_val = i
        for j in range(i + 1, len(lst)):
            if lst[min_val] > lst[j]:
                min_val = j
        if i != min_val:
            lst[i], lst[min_val] = lst[min_val], lst[i]

    return lst


print(selection_sort([4, 6, 2, 9, 1]))