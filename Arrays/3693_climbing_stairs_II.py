from typing import List
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        n = len(costs)

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            minimum = float('inf')

            if i - 1 >= 0:
                minimum = min(minimum, dp[i - 1] + costs[i - 1] + 1**2)

            if i - 2 >= 0:
                minimum = min(minimum, dp[i - 2] + costs[i - 1] + 2**2)

            if i - 3 >= 0:
                minimum = min(minimum, dp[i - 3] + costs[i - 1] + 3**2)

            dp[i] = minimum

        return dp[n]