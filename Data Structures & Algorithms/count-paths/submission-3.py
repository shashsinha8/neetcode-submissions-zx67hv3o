class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # ans = [[1 if (j == 0 or i == 0) else 0 for j in range(n)] for i in range(m)]
        
        ans = [1] * n

        for r in range(1, m): 
            temp = 1 
            for c in range(1, n):
                ans[c] += temp
                temp = ans[c]
            
        print(ans)
        return ans[n-1]

