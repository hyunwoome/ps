import sys

N = int(sys.stdin.readline())
paths = sys.stdin.readline().split()

x, y = 1, 1

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

nx, ny = 0, 0

for path in paths:
    for i in range(len(move)):
        if path == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny

print(x, y)