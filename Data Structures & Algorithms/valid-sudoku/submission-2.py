class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            cols = []
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in cols:
                    return False
                cols.append(board[i][j])
        for i in range(9):
            rows =[]
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in rows:
                    return False
                rows.append(board[j][i])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                mtx = []
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        if board[row][col] == '.':
                            continue
                        if board[row][col] in mtx:
                            return False
                        mtx.append(board[row][col])
        return True
