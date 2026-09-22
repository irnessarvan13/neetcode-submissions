class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)    # rows[0] = set of numbers in row 0
        cols = defaultdict(set)    # cols[0] = set of numbers in col 0
        boxes = defaultdict(set)   # boxes[(0,0)] = set of numbers in top-left box
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rows[r] or val in cols[c] or val in boxes[(r//3, c//3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r//3, c//3)].add(val)
        return True
