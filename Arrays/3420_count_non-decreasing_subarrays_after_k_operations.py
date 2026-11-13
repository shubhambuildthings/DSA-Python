from typing import List
from collections import deque
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        operations = 0
        right = len(nums) - 1
        blocks = deque()

        for left in range(len(nums) - 1, -1, -1):
            value = nums[left]
            count = 1

            # Merge the suffix blocks that must be raised to value.
            while blocks and blocks[-1][0] < value:
                block_value, block_count = blocks.pop()
                count += block_count
                operations += (value - block_value) * block_count
            blocks.append((value, count))

            # Remove elements from the right until this window is affordable.
            while operations > k:
                block_value, block_count = blocks.popleft()
                operations -= block_value - nums[right]
                if block_count > 1:
                    blocks.appendleft((block_value, block_count - 1))
                right -= 1

            ans += right - left + 1

        return ans