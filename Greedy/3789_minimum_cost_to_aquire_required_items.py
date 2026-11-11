class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        common = min(need1, need2)
        remaining1 = need1 - common
        remaining2 = need2 - common

        total = (
                common * min(costBoth, cost1 + cost2)
                + remaining1 * min(cost1, costBoth)
                + remaining2 * min(cost2, costBoth)
        )

        return total
