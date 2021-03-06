class Solution:
    def minPathSum(self, grid):
        """O(m*n) time | O(m) space | for an m*n matrix"""
        if not grid or not grid[0]: return
        rows = len(grid)
        cols = len(grid[0])
        
        prev = [float('inf')] * cols
        prev[0] = 0
        for r in range(rows):
            current = [0] * (cols)
            for c in range(cols):
                if c == 0:
                    current[c] = grid[r][c] + prev[c]
                else:
                    current[c] = min(grid[r][c] + prev[c], grid[r][c] + current[c-1])
            prev = current
        return prev[-1]
