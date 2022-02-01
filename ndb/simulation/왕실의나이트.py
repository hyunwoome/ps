def solution(loc):
    moves = [
        [2, 1], [2, -1], [-2, 1], [-2, -1],
        [1, 2], [1, -2], [-1, 2], [-1, -2],
    ]
    answer = 0
    location = list(map(int, str(ord(loc[0]) - 96) + loc[1]))
    for lo in moves:
        x = location[0] + lo[0]
        y = location[1] + lo[1]
        if x > 8 or x <= 0 or y > 8 or y <= 0:
            continue
        else:
            answer += 1

    return answer


print(solution('a1'))
