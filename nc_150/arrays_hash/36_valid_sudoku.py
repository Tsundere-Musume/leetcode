from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                cur = board[i][j]
                if (cur == "."):
                    continue
                g = ((i // 3) * 3) + (j//3)
                if (cur in row[i] or cur in col[j] or cur in grid[g]):
                    return False 
                row[i].add(cur)
                col[j].add(cur)
                grid[g].add(cur)
        return True
        
