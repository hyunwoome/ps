N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_a = sorted(a)  # [1, 2, 5, 4, 3]
sorted_b = sorted(b, reverse=True)  # [6, 6, 5, 5, 5]

for i in range(K):
    sorted_a[i] = sorted_b[i]

print(sum(sorted_a))
