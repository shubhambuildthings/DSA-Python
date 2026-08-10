from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maximum = max(nums)
        minimum = min(nums)
        
        for e in nums:
            if e != minimum and e != maximum:
                return e

        return -1