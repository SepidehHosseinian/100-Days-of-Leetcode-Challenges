from ast import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=defaultdict(set)
        rows=defaultdict(set)
        boxes=defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                medium = board[r][c]
                if medium==".":
                    continue
                    
                if medium in rows[r] or medium in cols[c] or medium in boxes[(r//3), c//3]:
                    return False
                
                else:
                    cols[c].add(medium)
                    rows[r].add(medium) 
                    boxes[(r//3), c//3].add(medium) 
                    
        return True