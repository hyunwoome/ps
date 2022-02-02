class Solution:
    def kClosest(self, points, k):
        def cal_dist(point):
            return point[0] * point[0] + point[1] * point[1]

        answer = []

        # 각 좌표를 제곱한 합을 저장할 리스트 tmp
        tmp = []
        for i in points:
            tmp.append(cal_dist(i))

        # 각 좌표를 저장한 리스트 tmp를 오름차순으로 정렬
        sorted_tmp = sorted(tmp)

        # 오름차순으로 정렬된 좌표의 합에서 k번째 수를 구함
        kth = 0
        for i in range(len(sorted_tmp)):
            if i == k - 1:
                kth = sorted_tmp[i]

        # k번째 수를 구했으면 이제 정렬되기 전(points와 동일한 순서를 가진) tmp에서
        # k번째 수보다 작은 값의 인덱스를 구할 수 있고, 그 인덱스를 기존 points에 할당하면
        # k번째 이하의 좌표들을 뽑아낼 수 있다.
        for i in range(len(tmp)):
            if tmp[i] <= kth:
                answer.append(points[i])

        return answer