from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_first():
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    answer = mid
                    right = mid - 1 #keep looking to the left

                elif nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return answer

        def find_last():
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    answer = mid
                    left = mid + 1 # keep looking to the right

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return answer

        return[find_first(), find_last()]

