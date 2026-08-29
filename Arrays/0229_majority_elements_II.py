from typing import List
class Solution:
    def majorityElements(self, nums: List[int]) -> List[int]:
        candidate1, count1 = [], 0
        candidate2, count2 = [], 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

            result = [candidate1, candidate2]

        return [num for num in result if nums.count(num) > len(nums) // 3]