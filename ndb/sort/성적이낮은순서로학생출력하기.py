N = int(input())
arr = []
for i in range(N):
    data = input().split()
    arr.append((data[0], data[1]))

arr = sorted(arr, key=lambda score: score[1])

for i in arr:
    print(i[0], end=' ')