def solution():
    n, m = map(int, input().split(' '))
    dict = {}
    for _ in range(0, n):
        site, ps = input().split(' ')
        dict[site] = ps

    for _ in range(0, m):
        site_input = input()
        print(dict[site_input])

solution()