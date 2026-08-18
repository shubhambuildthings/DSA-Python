from typing import List
class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        neg = 0
        pos = 0

        for num in nums:
            if num > 0:
                pos += 1

            if num < 0:
                neg += 1

        if pos > neg:
            return pos
        else:
            return neg