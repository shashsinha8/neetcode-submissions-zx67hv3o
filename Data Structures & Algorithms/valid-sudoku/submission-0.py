class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        

        # row 1-9
        for row in range(9):
            seen = set()
            # board[i] = ["1","2",".",".","3",".",".",".","."]
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        # col 1-9
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # 3x3 logic
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3+i
                    col = (square%3)*3+j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
                    
        return True

