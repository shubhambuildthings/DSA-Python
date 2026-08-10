from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        answer = [[], []]
        answer[0] = []
        answer[1] = []

        for e in set1:
            if e not in set2:
                answer[0].append(e)

        for e in set2:
            if e not in set1:
                answer[1].append(e)

        return answer
