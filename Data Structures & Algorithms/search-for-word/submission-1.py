class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] != word[i]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"  # mark visited
            
            neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in neighbors:
                nr, nc = r+dr, c+dc
                if dfs(nr, nc, i+1):  # recurse to next character
                    board[r][c] = temp
                    return True
            
            board[r][c] = temp  # backtrack
            return False

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False