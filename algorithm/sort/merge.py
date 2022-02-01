def merge_sort(lst):
    def merge(left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    L = lst[:mid]
    R = lst[mid:]
    return merge(merge_sort(L), merge_sort(R))


print(merge_sort([4, 6, 2, 9, 1]))
