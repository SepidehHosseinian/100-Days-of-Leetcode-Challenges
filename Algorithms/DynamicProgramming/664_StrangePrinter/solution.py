class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                dp[i][j] = dp[i][j-1] + 1
                for k in range(i, j):
                    if s[k] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + (dp[k+1][j-1] if k+1<=j-1 else 0))

        return dp[0][n-1]