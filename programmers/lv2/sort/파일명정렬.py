# HEAD: 사전 순 정렬 (대소비교x)
# NUMBER: 오름차순
# TAIL: TAIL은 무시, HEAD와 NUMBER가 같을경우 원래 입력에 주어진 순서를 유지한다.
import re


def solution(files):
    temp = [re.split(r"(\d+)", s) for s in files]
    sorting_arr = sorted(temp, key=lambda k: (k[0].lower(), int(k[1])))
    answer = []
    for i in sorting_arr:
        answer.append("".join(i))
    return answer


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
