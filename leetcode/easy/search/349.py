import bisect


class Solution:
    def intersection(self, nums1, nums2):
        # 각 배열의 중복값을 제거하고 정렬
        li1 = sorted(list(set(nums1)))  # [4, 5, 9]
        li2 = sorted(list(set(nums2)))  # [4, 8, 9]

        result = []

        for i in li1:
            # bisect_left를 사용해서 포함여부를 확인
            idx = bisect.bisect_left(li2, i)
            if idx < len(li2) and li2[idx] == i:
                result.append(i)

        return result


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
sol = Solution()
print(sol.intersection(nums1, nums2))
