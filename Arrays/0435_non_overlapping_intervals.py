# Remember this Greedy rule
# When two intervals overlap, prefer the one with the smaller ending point.
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        count = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]

            if start < end:
                count += 1

            else:
                end = intervals[i][1]

        return count