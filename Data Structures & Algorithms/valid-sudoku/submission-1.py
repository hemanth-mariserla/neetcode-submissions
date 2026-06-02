from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            d = defaultdict(int)
            for j in range(len(board[i])):
                if d[board[i][j]] >= 1 and board[i][j] != '.':
                    return False
                else:
                    d[board[i][j]] += 1
        for i in range(len(board[0])):
            d = defaultdict(int)
            for j in range(len(board)):
                if d[board[j][i]] >= 1 and board[j][i] != '.':
                    return False
                else:
                    d[board[j][i]] += 1
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                d = defaultdict(int)
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if d[board[k][l]] >= 1 and board[k][l] != '.':
                            return False
                        else:
                            d[board[k][l]] += 1
        return True
