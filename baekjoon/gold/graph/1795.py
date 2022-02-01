"""
주어진 C개의 문자 중에서 L개의 문자를 뽑아
2가지 조건에 부합하는 비밀번호 문자열을 알파벳 순서로 출력
"""
# 조건
# 1. 최소 한 개의 모음 (a, e, i, o u)
# 2. 최소 두 개의 자음
# 3. 알파벳 순서대로

def solution():
    """
    L : 비밀번호의 개수
    C : 주어진 문자의 개수
    vowels : 알파벳 모음
    """
    L, C = map(int, input().split())
    char = list(input().split())
    char.sort()
    vowels = ['a', 'e', 'i', 'o', 'u']
    answer = []

    # --------------------------dfs,bfs------------------------- #

    def DFS(pw, index):
        # 추측한 비밀번호 개수와 구해야 하는 비밀번호의 개수가 일치할 때
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

        # 추측한 비밀번호 개수와 구해야 하는 비밀번호의 개수가 일치하지 않을 때
        for i in range(index, C):
            answer.append(char[i])
            DFS(pw + 1, i + 1)
            # pop : pw의 개수를 줄여 다음 문자열을 넣을 수 있게하기 위함
            answer.pop()
    # --------------------------dfs,bfs------------------------- #

    DFS(0, 0)


solution()
