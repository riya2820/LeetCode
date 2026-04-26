class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        if len(board) != 8 or len(board[0]) != 8:
            return -1

        count = 0 
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R': # rook found
                    # check up 
                    for k in range(r-1, -1, -1):
                        if board[k][c] == 'B':
                            break
                        elif board[k][c] == 'P' or board[k][c] == 'p':
                            count += 1
                            break
                    # check down
                    for k in range(r+1, 8, 1):
                        if board[k][c] == 'B':
                            break
                        elif board[k][c] == 'P' or board[k][c] == 'p':
                            count += 1
                            break
                    # check left 
                    for k in range(c-1, -1, -1):
                        if board[r][k] == 'B':
                            break
                        elif board[r][k] == 'P' or board[r][k] == 'p':
                            count += 1
                            break
                    # check right
                    for k in range(c+1, 8, 1):
                        if board[r][k] == 'B':
                            break
                        elif board[r][k] == 'P' or board[r][k] == 'p':
                            count += 1
                            break
        return count