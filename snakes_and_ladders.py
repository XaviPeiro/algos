from typing import List
from collections import deque

class Solution:
    def __call__(self, board: List[List[int]]) -> int:    
        n_cells = deque()
        n_cells.append((len(board)-1, 0, 0))
    
        while n_cells:
            n_cell = n_cells.popleft()
            row, col = n_cell[0], n_cell[1]
            cells = self.get_next(board, row, col)

            for c in cells:
                if c[0] == 0 and c[1] == self.get_end_col(board):
                    return n_cell[2]+1
                n_cells.append((c[0], c[1], n_cell[2]+1))
        return 0

    def get_end_col(self, board):
        if self.get_sense(board, 0) == 1:
            return len(board)-1
        return 0
    def get_sense(self, board, row):
        return 1 if (len(board)-1)%2 == row%2 else -1

    def get_next(self, board, row, col):
        sense = self.get_sense(board, row)

        res = []
        for i in range(6):
            if not 0 <= col+sense <= len(board)-1:
                row -= 1
                col = 0 if sense==-1 else len(board)-1
            else:
                col += sense
            
            if not 0 <= row <= len(board)-1:
                print("Out of the board")
                break
            
            if board[row][col] != -1:
                nrow, ncol = self.number_to_coor(board, board[row][col])
                res.append((nrow, ncol))
            elif i == 5:
                res.append((row, col))
            
        return res

    def number_to_coor(self, board, n: int):
        row, col = divmod(n, len(board))
        if col == 0:
            row -= 1
            if self.get_sense(board, row) == 1:
                col = len(board)-1
            else:
                col = 0
        else:
            if self.get_sense(board, row) == 1:
                col = col - 1
            else:
                col = (len(board)-1-col)+1
            col -= 1
            
        return (row, col)
        
if __name__ == "__main__":
    # s = Solution()
    # board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

    # assert s(board) == 4, s(board)
    s = Solution()
    board = [[-1,-1],[-1,3]]

    assert s(board) == 1, s(board)