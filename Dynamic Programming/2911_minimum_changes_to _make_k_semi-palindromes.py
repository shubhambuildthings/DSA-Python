#with the help of chatgpt, i was able to solve this problem.
# The key idea is to use dynamic programming to calculate the minimum number of changes needed to make the string a k-semi-palindrome.
# We first calculate the cost of making each substring a semi-palindrome and then use that information to fill in the dp table.

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = INF

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for r in range(d):
                        left = i + r
                        right = j - ((length - 1 - r) % d)

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for t in range(1, k + 1):
            for i in range(2 * t, n + 1):
                for j in range(2 * (t - 1), i - 1):
                    if cost[j][i - 1] != INF:
                        dp[i][t] = min(
                            dp[i][t],
                            dp[j][t - 1] + cost[j][i - 1]
                        )

        return dp[n][k]