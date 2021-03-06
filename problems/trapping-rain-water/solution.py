class Solution:
    def trap(self, height) -> int:
        """O(n) time and space"""
        maxh = 0
        forward_trap = [0] * len(height)
        for i, h in enumerate(height):
            maxh = max(maxh, h)
            forward_trap[i] = maxh - h
        trapped = 0
        maxh = 0
        for i in range(len(height)-1, -1, -1):
            h = height[i]
            maxh = max(maxh, h)
            trapped += min(forward_trap[i], (maxh - h))
        return trapped
