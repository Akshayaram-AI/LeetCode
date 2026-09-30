class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removed = 0
        end = float("-inf")
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                removed += 1
        return removed