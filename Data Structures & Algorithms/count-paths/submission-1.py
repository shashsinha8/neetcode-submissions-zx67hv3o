class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # ans = [[1 for j in range(n) if j == 0 else 1] for i in range(m)]
        ans = [[1 if (j == 0 or i == 0) else 0 for j in range(n)] for i in range(m)]

        def dfs(r,c):
            ans[r][c] = ans[r-1][c] + ans[r][c-1]
            return
        
        for r in range(1, m): 
            for c in range(1, n):
                dfs(r,c)
            
        print(ans)
        return ans[m-1][n-1]

