from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        """O(n) time | O(u) space | u -> unique nums"""
        counts = Counter(nums)
        return [x for x, y in counts.most_common(k)]
