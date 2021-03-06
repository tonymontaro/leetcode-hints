from collections import defaultdict

class Solution:
    def hIndex(self, citations) -> int:
        """O(n) time and space (bucket sort)"""
        if not citations: return 0
        buckets = defaultdict(int)
        for num in citations:
            buckets[min(num, len(citations))] += 1
        total = 0
        for i in range(max(buckets.keys()), -1, -1):
            total += buckets[i]
            if total >= i:
                return i
        return 0
