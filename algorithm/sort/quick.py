# 퀵 정렬
# 최악- n^2, 최선- n log n
# 분할정복 알고리즘이며, 피벗을 기준으로 작은 집합, 큰 집합으로 나눠 재귀적으로 정렬 실행

def quick_sort(lst, start, end):
    def partition(low, high):
        pivot = lst[high]
        left = low
        for right in range(low, high):
            if lst[right] < pivot:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1

        lst[left], lst[high] = lst[high], lst[left]
        return left

    if start < end:
        pivot = partition(start, end)
        quick_sort(lst, start, pivot - 1)
        quick_sort(lst, pivot + 1, end)

    return lst


print(quick_sort([1, 6, 2, 9, 4], 0, 4))
