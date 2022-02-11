def solution(n, times):
    answer = 0
    # 이진 탐색에서 범위 잡기
    # 입국 심사로 소요되는 시간은 1부터 최대 60까지 소요될 수 있음
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        people = 0
        for i in times:
            # 이진 탐색이므로 반(mid)에 기준점을 두고 탐색
            # mid를 7과 10으로 나누면 해당 분에 각각 몇 명을 처리할 수 있는지 알 수 있다.
            people += mid // i
            if people >= n:
                break

        # 반을 기준으로 처리할 수 있는 사람 수가 n보다 같거나 크다면,
        # 시간이 여유있는 것으로 간주할 수 있으므로 범위를 아래로 좁힌다.
        if people >= n:
            answer = mid
            right = mid - 1

        # 반을 기준으로 처리할 수 있는 사람 수가 n보다 작다면,
        # n만큼 처리하기에 시간이 부족한 것으로 간주할 수 있으므로 범위를 위로 좁힌다.
        elif people < n:
            left = mid + 1

    return answer

n = 6
times = [7, 10]
print(solution(n, times))
