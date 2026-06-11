class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        ans = [[1 if (j == 0 or i == 0) else 0 for j in range(n)] for i in range(m)]
        
        for r in range(1, m): 
            for c in range(1, n):
                ans[r][c] = ans[r-1][c] + ans[r][c-1]
            
        print(ans)
        return ans[m-1][n-1]

