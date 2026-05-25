class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
 
        def bfs(r, c):
            
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            q = deque()
            q.append((r, c))
            visited.add((r,c))
            while q: 
                row, col = q.popleft()
                for dr, dc in directions: 
                    nr, nc = row + dr, col + dc
                    if (
                        (nr, nc) not in visited and
                        0 <= nr < rows and 
                        0 <= nc < cols and grid[nr][nc] == "1"
                        ):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        ans = 0

        for r in range(rows):
            for c in range(cols):
                if (
                    grid[r][c] == "1" and 
                    (r, c) not in visited
                ):
                    bfs(r, c)
                    ans += 1
        return ans
                    


