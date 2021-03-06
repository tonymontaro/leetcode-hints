class Solution:
    def maximalSquare(s, matrix) -> int:
        """O(r*c) time and space | r->rows, c->cols"""
        if not matrix: return 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = int(matrix[row][col])
                if matrix[row][col] == 1 and row > 0 and col > 0:
                    matrix[row][col] = 1 + min(
                        matrix[row-1][col], matrix[row-1][col-1], matrix[row][col-1])
        return max(max(row) for row in matrix)**2
