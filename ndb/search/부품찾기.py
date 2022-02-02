N = int(input())
N_arr = sorted(list(map(int, input().split())))
M = int(input())
M_arr = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end:
        return 'no'

    mid = (start + end) // 2

    if array[mid] == target:
        return 'yes'

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    else:
        return binary_search(array, target, mid + 1, end)


for i in M_arr:
    print(binary_search(N_arr, i, 0, N), end=' ')

    # no yes yes
