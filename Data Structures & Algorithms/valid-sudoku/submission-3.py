class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        # for i in range(9):
        #     row = set()
        #     count = 0
        #     for j in range(9):
        #         if board[i][j].isnumeric():
        #             count += 1
        #             row.add(board[i][j])
        #     print(f"count = {count} and row len = {len(row)}")
        #     if len(row) != count:
        #         return False
        
        # print()
        # for i in range(9):
        #     col = set()
        #     count = 0
        #     for j in range(9):
        #         if board[j][i].isnumeric():
        #             count += 1
        #             col.add(board[j][i])
        #     print(f"count = {count} and col len = {len(col)}")
        #     if len(col) != count:
        #         return False
        
        # print()
        # squares = collections.defaultdict(set)

        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] == '.':
        #             continue
        #         if board[i][j] in squares[(i // 3,j//3)]:
        #             return False
        #         squares[(i//3,j//3)].add(board[i][j])
        # return True 
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if ( board[r][c] in rows[r]
                         or board[r][c] in cols[c]
                         or board[r][c] in squares[(r//3, c//3)]):
                         return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
        return True