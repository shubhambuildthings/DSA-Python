from typing import List
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:

        nums = [0 if x % 2 == 0 else 1 for x in nums]
        nums.sort()

        return nums