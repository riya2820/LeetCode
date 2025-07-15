class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # grid[m-1][n-1] i.e either right or down 
        result = 0
        dp = [[1]*n for r in range(m)]

        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c]+dp[r][c-1]
            
        return dp[-1][-1]
      
# O(n*m) space and time complexity 
