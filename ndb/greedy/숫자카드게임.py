def solution(card):
    min_val = []
    for i in card:
        min_val.append(min(i))
    return max(min_val)


# lst = [
#     [3, 1, 2],
#     [4, 1, 4],
#     [2, 2, 2]
# ]
lst = [
    [7, 3, 1, 8],
    [3, 3, 3, 4]
]
print(solution(lst))
