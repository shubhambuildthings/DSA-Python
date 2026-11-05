import heapq
from collections import defaultdict


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        # Quick pruning: if the array cannot fit k non-overlapping windows of size x
        if n < x * k:
            return -1

        # Step 1: Sliding Window using Two Heaps with Lazy Deletion
        # left_heap (max-heap) stores the smaller half of the elements
        # right_heap (min-heap) stores the larger half of the elements
        left_heap = []
        right_heap = []

        left_sum = 0
        right_sum = 0

        # Track counts of elements that need to be lazily deleted
        to_delete = defaultdict(int)

        # Keep track of active sizes of the heaps
        left_size = 0
        right_size = 0

        min_ops = [float('inf')] * n

        def balance():
            nonlocal left_size, right_size, left_sum, right_sum
            # Clean up the tops of heaps if they contain elements marked for deletion
            while left_heap and to_delete[-left_heap[0]] > 0:
                val = -heapq.heappop(left_heap)
                to_delete[val] -= 1
            while right_heap and to_delete[right_heap[0]] > 0:
                val = heapq.heappop(right_heap)
                to_delete[val] -= 1

            # Maintain the size property: left_size can be equal to or 1 greater than right_size
            if left_size > right_size + 1:
                val = -heapq.heappop(left_heap)
                heapq.heappush(right_heap, val)
                left_sum -= val
                right_sum += val
                left_size -= 1
                right_size += 1
            elif right_size > left_size:
                val = heapq.heappop(right_heap)
                heapq.heappush(left_heap, -val)
                right_sum -= val
                left_sum += val
                right_size -= 1
                left_size += 1

            # Secondary cleanup after structural shifts
            while left_heap and to_delete[-left_heap[0]] > 0:
                val = -heapq.heappop(left_heap)
                to_delete[val] -= 1
            while right_heap and to_delete[right_heap[0]] > 0:
                val = heapq.heappop(right_heap)
                to_delete[val] -= 1

        for i, num in enumerate(nums):
            # Insert the new element into the tracking system
            if not left_heap or num <= -left_heap[0]:
                heapq.heappush(left_heap, -num)
                left_sum += num
                left_size += 1
            else:
                heapq.heappush(right_heap, num)
                right_sum += num
                right_size += 1

            # If window exceeds size x, lazily remove the oldest element
            if i >= x:
                old_num = nums[i - x]
                to_delete[old_num] += 1

                # Check where it was logically sitting to decrement tracking size/sums
                if left_heap and old_num <= -left_heap[0]:
                    left_sum -= old_num
                    left_size -= 1
                else:
                    right_sum -= old_num
                    right_size -= 1

            balance()

            # When a full window of size x is formed
            if i >= x - 1:
                median = -left_heap[0]
                # Formula: Cost to make all elements equal to the median
                cost = (median * left_size - left_sum) + (right_sum - median * right_size)
                min_ops[i - x + 1] = cost

        # Step 2: Dynamic Programming to choose k non-overlapping windows
        # dp[i][j] represents the minimum cost choosing j subarrays from suffix nums[i:]
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

        # Base case: 0 subarrays required costs 0 operations for any suffix
        for i in range(n + 1):
            dp[i][0] = 0

        for j in range(1, k + 1):
            for i in range(n - 1, -1, -1):
                # Option 1: Skip the current index
                res = dp[i + 1][j]

                # Option 2: Form a valid subarray starting at index i
                if i + x <= n and min_ops[i] != float('inf'):
                    res = min(res, min_ops[i] + dp[i + x][j - 1])

                dp[i][j] = res

        ans = dp[0][k]
        return ans if ans != float('inf') else -1