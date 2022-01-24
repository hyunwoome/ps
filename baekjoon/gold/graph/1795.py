# 1. 최소 한 개의 모음 (a, e, i, o u)
# 2. 최소 두 개의 자음
# 3. 알파벳 정렬
# 4. L개로 구성됨

def solution():
    L, C = map(int, input().split())
    char = list(input().split())
    char.sort()
    vowels = ['a', 'e', 'i', 'o', 'u']
    answer = []

    def dfs(pw, index):
        # 4 == 4
        if pw == L:
            vo = 0
            co = 0
            for i in range(len(answer)):
                if answer[i] in vowels:
                    vo += 1
                else:
                    co += 1

            if vo >= 1 and co >= 2:
                print(''.join(answer))

            return

        # 4 != 4
        for i in range(index, C):
            answer.append(char[i])
            dfs(pw + 1, i + 1)
            answer.pop()

    dfs(0, 0)


solution()
