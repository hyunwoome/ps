def solution(progresses, speeds):
    answer = []

    while progresses:

        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]

        count = 0
        while progresses:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                break

        if count:
            answer.append(count)

    return answer


pro = [93, 30, 55]
spe = [1, 30, 5]
print(solution(pro, spe))
