# Problem found at: https://leetcode.com/problems/valid-sudoku/submissions/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Checks each row. 
        for row in board:
            row = [cell for cell in row if cell != '.']
            if len(row) != len(set(row)):
                return False
        
        # Checks each column. 
        for y in range(9):
            column = set()
            for x in range(9):
                cell_value = board[x][y]
                if cell_value in column:
                    return False
                if cell_value != '.':
                    column.add(cell_value)
        
        # Creates a function to check squares. 
        def check_square(x, y):
            square = set()
            for z in range(x, x + 3):
                for p in range(y, y + 3):
                    sq_cell_value = board[z][p]
                    if sq_cell_value in square:
                        return False
                    if sq_cell_value != '.':
                        square.add(sq_cell_value)
            return True
        
        # Checks each square. 
        for x in range(0,9,3):
            for y in range(0,9,3):
                if not check_square(x, y):
                    return False
        
        return True
      
