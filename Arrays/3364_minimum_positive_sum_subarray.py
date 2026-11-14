from typing import List
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')

        for i in range(len(nums)):
            subarray_sum = 0
            for j in range(len(nums)):
                if i <= j:
                    subarray_sum += nums[j]
                    if l <= j -i + 1 <= r and subarray_sum > 0:
                        ans = min(ans, subarray_sum)

        return ans if ans != float('inf') else -1