def solution(location, direction, map):
    d = [[0] * len(map) for _ in map]
    x, y = location
    d[x][y] = 1  # 방문처리

    # 북, 동, 남, 서 위치
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    def turn_left():
        global direction
        direction -= 1
        if direction == -1:
            direction = 3

    count = 1
    turn_time = 0
    while True:
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]
        if d[nx][ny] == 0 and map[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        else:
            turn_time += 1

        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]

            if map[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

    return count


location = [1, 1]
direction = 0
map = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
print(solution(location, direction, map))