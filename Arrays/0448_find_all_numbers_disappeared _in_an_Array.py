from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_Set = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in nums_Set:
                result.append(i)

        return result
