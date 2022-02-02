N, M = list(map(int, input().split()))
N_arr = list(map(int, input().split()))


def binary_search(array, target, start, end):
    mid = (start + end) // 2

    remain_val = 0
    for i in array:
        if i - mid > 0:
            remain_val += (i - mid)

    if remain_val == target:
        return mid
    elif remain_val > target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


print(binary_search(N_arr, M, 0, max(N_arr)))
