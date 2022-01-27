def solution(dirs):
    answer = 0
    start = [0, 0]
    hist = []

    for i in dirs:
        end = []
        if i == 'U':
            end = [start[0], start[1] + 1]
        elif i == 'D':
            end = [start[0], start[1] - 1]
        elif i == 'L':
            end = [start[0] - 1, start[1]]
        elif i == 'R':
            end = [start[0] + 1, start[1]]

        if end[0] > 5 or end[0] < -5 or end[1] > 5 or end[1] < -5:
            continue

        route = [start, end]
        start = end

        if route not in hist and route[::-1] not in hist:
            hist.append(route)
            answer += 1

    return answer


print(solution('LRLRL'))
