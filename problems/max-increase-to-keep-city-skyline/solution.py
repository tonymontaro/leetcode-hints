from collections import defaultdict

def maxIncreaseKeepingSkyline(grid):
    """O(N*M) time | O(N + M) space"""
    max_rows = defaultdict(int)
    max_cols = defaultdict(int)
    for r in range(len(grid)):
        for c in range(len(grid)):
            max_rows[r] = max(max_rows[r], grid[r][c])
            max_cols[c] = max(max_cols[c], grid[r][c])
    increases = 0
    for r in range(len(grid)):
        for c in range(len(grid)):
            max_val = min(max_rows[r], max_cols[c])
            increases += max_val - grid[r][c]
    return increases
