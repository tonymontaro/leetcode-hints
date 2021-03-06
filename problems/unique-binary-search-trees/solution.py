class Solution:
    def numTrees(self, num: int) -> int:
        """O(n^2) time | O(n) space"""
        cache = {}
        cache[0] = 1
        for n in range(1, num+1):
            total = 0
            for i in range(1, n+1):
                total += cache[i-1] * cache[n-i]
            cache[n] = total
        return cache[num]
