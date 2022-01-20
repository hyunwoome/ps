def solution(progresses, speeds):
    """
    1. 100이 되면 기능개발 완료
    2. 완료되더라도 앞에 완료가 안된 작업이 있다면 대기
    """
    answer = []
    while len(progresses) > 0:

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
        if count > 0:
            answer.append(count)
    return answer








progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
