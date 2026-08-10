from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums)
        unique_list = []

        for e in nums_set:
            unique_list.append(e)

        unique_list = sorted(unique_list)

        if len(unique_list) >= 3:
            return unique_list[-3]
        else:
            return unique_list[-1]