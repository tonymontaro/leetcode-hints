from collections import Counter

class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        """O(n) time | O(1) space"""
        if not tasks: return 0
        counts = Counter(tasks).values()
        max_count = max(counts)
        max_count_nums = list(counts).count(max_count)
        return max(len(tasks), ((max_count-1)*(n+1) + max_count_nums))
