# 순환구조 판별
import collections



class Solution:
    def canFinish(self, numCourses, prerequisites):

        def dfs(node):
            # 사이클 찾기
            if visited[node]:
                return False

            visited[node] = 1
            for nbr in dic[node]:
                if visited[nbr] != 2 and not dfs(nbr):
                    return False

            visited[node] = 2
            return True

        if not prerequisites:
            return True

        # 인접 리스트
        dic = collections.defaultdict(list)  # { 1: [0], 0: [1] }
        for x, y in prerequisites:
            dic[x].append(y)

        visited = [0] * numCourses  # [0 ,0]

        for node in list(dic):  # 1
            # 방문을 아직 안했고
            if not visited[node]:
                # dfs가 false가 아니라면
                if not dfs(node):
                    return False

        return True



numCourses = 2
prerequisites = [[1, 0], [0, 1]]
sol = Solution()
print(sol.canFinish(numCourses, prerequisites))
