from typing import List
class Solution:
    def rankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        nums = {}
        rank = 1

        for num in sorted_arr:
            if num not in nums:
                nums[num] = rank
                rank += 1

        answer = []

        for num in arr:
            answer.append(nums[num])

        return answer