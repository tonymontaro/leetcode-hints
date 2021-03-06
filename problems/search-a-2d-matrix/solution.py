class Solution:
    def searchMatrix(self, matrix, target):
        """O(logn) time | O(1) space"""
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows*cols-1
        while left <= right:
            mid = (left + right) // 2
            col, row = mid % cols, mid // cols
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                right = mid-1
            else:
                left = mid+1
        return False
