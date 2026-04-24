class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid: 
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row = row - dr
                    new_col = col - dc
                    if (
                        new_row in range(ROWS) and
                        new_col in range(COLS) and
                        (new_row, new_col) not in visited and
                        grid[new_row][new_col] == "1"
                        ):
                        q.append((new_row,new_col))
                        visited.add((new_row, new_col))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
                
        return islands
                    