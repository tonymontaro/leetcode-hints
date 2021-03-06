class Solution:
    def merge(self, intervals):
        """O(nlogn) time and space"""
        if not intervals: return []
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        current = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if current[0] <= start <= current[1]:
                current = [current[0], max(current[1], end)]
            else:
                result.append(current)
                current = [start, end]
        result.append(current)
        return result
