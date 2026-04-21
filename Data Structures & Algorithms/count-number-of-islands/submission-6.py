class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid: 
            return 0


        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()
        
        def search(r,c):

            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            
            while q: 
                qr, qc = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = qr+dr, qc+dc
                    if (
                        new_row in range(rows) and
                        new_col in range(cols) and
                        (new_row, new_col) not in visited and
                        grid[new_row][new_col] == "1"
                    ):
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    search(r,c)
                    islands += 1
        return islands

