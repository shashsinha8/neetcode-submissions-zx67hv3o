import sys
sys.setrecursionlimit(20000)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:


        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        ROWS = len(matrix)
        COLS = len(matrix[0])
        visited = {}
        

        def dfs(r, c):

            if (r,c) in visited:
                return visited[(r,c)]

            currlong = 1
            for dr, dc in directions:
                nr, nc = dr+r, c+dc
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    matrix[nr][nc] > matrix[r][c]
                ):
                    currlong = max(currlong, 1 + dfs(nr, nc))
            visited[(r, c)] = currlong
            return currlong
        
        ans = 1
        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, dfs(r, c))

        return (ans)