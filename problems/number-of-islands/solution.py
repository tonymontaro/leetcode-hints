class Solution:
    def numIslands(self, grid) -> int:
        """O(n) time and space"""
        islands = 0
        self.seen = {}
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row, col) not in self.seen and grid[row][col] == '1':
                    islands += 1
                    self.explore(row, col, grid)
        return islands
    
    def explore(self, row, col, grid):
        is_valid_loc = row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0
        if is_valid_loc or (row, col) in self.seen or grid[row][col] == '0':
            return
        self.seen[(row, col)] = True
        self.explore(row+1, col, grid)
        self.explore(row, col+1, grid)
        self.explore(row-1, col, grid)
        self.explore(row, col-1, grid)
