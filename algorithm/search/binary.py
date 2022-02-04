"""
이진 탐색은 정렬되어 있는 배열에서 원소를 O(log N)의
시간으로 탐색할 수 있는 알고리즘이다.
"""

def binary_search(arr, target):
    def bs(start, end):
        # 배열의 시작과 끝의 포인터를 설정하고,
        # 시작 포인터가 끝 포인터보다 크다면 찾고자 하는 원소가
        # 없는 것이므로 -1을 반환
        if start > end:
            return -1

        # 배열의 시작과 끝의 가운데를 mid로 설정
        mid = (start + end) // 2

        # mid 인덱스의 원소가 찾으려하는 target보다 크다면,
        # 배열의 중간 아래에 원소가 위치하게 되므로,
        # 범위를 시작부터 중간까지 설정해 재귀를 실행
        if arr[mid] > target:
            return bs(start, mid - 1)

        # mid 인덱스의 원소가 찾으려하는 target보다 작다면,
        # 배열의 중간 위에 원소가 위치하게 되므로,
        # 범위를 중간부터 끝까지 설정해 재귀를 실행
        elif arr[mid] < target:
            return bs(mid + 1, end)

        # mid가 target과 일치한다면, 해당 원소를 찾은 것이기 때문에
        # mid 인덱스를 반환
        else:
            return mid

    return bs(0, len(arr) - 1)


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))  # 6
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))  # -1

