# 길이가 짧은 것부터
# 길이가 같으면 사전 순

N = int(input())
lst = [input() for _ in range(N)]
set = set(lst)
new_lst = list(set)
new_lst.sort()
new_lst.sort(key=len)
[print(i) for i in new_lst]
