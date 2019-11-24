class Solution(object):
    def matrixScore(self, matrix):
        """O(n^2) time and space | for nxn matrix"""
        ln = len(matrix)
        for r in range(ln):
            if matrix[r][0] == 0:
                reverse_rows(matrix, r)

        col_matrix = [[matrix[r][c] for r in range(ln)] for c in range(len(matrix[0]))]

        for c in range(len(col_matrix)):
            if sum(col_matrix[c]) < ln/2:
                reverse_rows(col_matrix, c)
        matrix = [[col_matrix[r][c] for r in range(len(col_matrix))] for c in range(ln)]
        return sum([to_hex(row) for row in matrix])
    
def reverse_rows(matrix, i):
    matrix[i] = [0 if num == 1 else 1 for num in matrix[i]]

def to_hex(row):
    return int(''.join(map(str, row)), 2)


## More concise and better 
class Solution(object):
    def matrixScore(self, A):
        """O(n^2) time | O(1) space | for nxn matrix"""
        rows, cols = len(A), len(A[0])
        res = (1 << cols - 1) * rows # (1 << cols - 1) is the same as (2**(cols - 1))
        for c in range(1, cols):
            col_sum = sum([A[r][c] == A[r][0] for r in range(len(A))])
            res += (2**(cols-c-1)) * max(col_sum, (rows - col_sum))
        return res
