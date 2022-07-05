# Problem found at: https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        row_len = len(matrix[0])
        matrix_len = len(matrix)
        zero_cols = set()
        zero_rows = set()

        for row_idx in range(matrix_len):
            for col_idx in range(row_len):
                if matrix[row_idx][col_idx] == 0:
                    zero_cols.add(col_idx)
                    zero_rows.add(row_idx)

        for k in zero_rows:
            matrix[k] = [0] * row_len

        for k in zero_cols:
            for row_idx in range(matrix_len):
                matrix[row_idx][k] = 0
        
