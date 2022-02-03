def insertion_sort1(lst):
    for i in range(len(lst) - 1):
        next = i + 1
        for j in range(i, -1, -1):
            if lst[j] > lst[next]:
                lst[j], lst[next] = lst[next], lst[j]
                next = j
            else:
                break

    return lst


def insertion_sort2(lst):
    for idx in range(1, len(lst)):
        val = lst[idx]
        compare = idx - 1


        while lst[compare] > val and compare >= 0:
            lst[compare + 1] = lst[compare]
            compare -= 1

        lst[compare + 1] = val
    return lst


print(insertion_sort1([4, 6, 2, 9, 1]))
print(insertion_sort2([4, 6, 2, 9, 1]))
